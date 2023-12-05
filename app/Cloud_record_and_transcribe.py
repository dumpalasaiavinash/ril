def speech_to_text():
    import sounddevice as sd
    import numpy as np
    import soundfile as sf
    import os
    from google.cloud import speech
    from domain_specific_words import glossary,wells,terms,crucial_words,alphabets,numbers,additional_terms
    from combine_single_letter_words import combine_single_letter_words
    from get_similarity import find_most_similar_word,get_next_words

    # Set the path to your service account key file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_key/reliance-stt-39902e2b2216.json"
    recorded_file_name = "recorded_audio_old.flac"

    def record_until_silence(sample_rate=44100, silence_threshold=0.01):
        print("Recording...")

        audio_data = []
        silence_counter = 5

        def callback(indata, frames, time, status):
            if status:
                print(status, flush=True)
            audio_data.append(indata.copy())
            if np.max(np.abs(indata)) < silence_threshold:
                nonlocal silence_counter
                silence_counter += 1
            else:
                silence_counter = 0

        with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):
            sd.sleep(1000)  # Give some time for the stream to start
            while silence_counter < 30:  # Adjust the silence counter threshold based on your needs
                sd.sleep(100)

        print("Recording finished.")
        return np.concatenate(audio_data, axis=0)

    def save_audio_to_flac(audio_data, filename, sample_rate=44100):
        sf.write(filename, audio_data, sample_rate, format='flac')

    def cloud_speech_to_text(audio_input):
        # Imports the Google Cloud client library
        print("started Transcription")
        # Instantiates a client
        client = speech.SpeechClient()
        # # Load the audio file
        import io
        audio_file = audio_input
        with io.open(audio_file, 'rb') as f:
            content = f.read()

        # The name of the audio file to transcribe
        # gcs_uri = "gs://cloud-samples-data/speech/VER_video_series/Anu1.wav"
        # audio =  speech.RecognitionAudio(uri=gcs_uri)

        custom_vocabulary = [
                {
                    "phrases":crucial_words,
                    "boost":40
                },
                {
                    "phrases":terms,
                    "boost":30
                },
                {
                    "phrases":alphabets,
                    "boost":5
                },
                {
                    "phrases":numbers,
                    "boost":5
                },
                {
                    "phrases":glossary,
                    "boost":10
                },
                {
                    "phrases":additional_terms,
                    "boost":5
                },
                 
                ]
        audio =  speech.RecognitionAudio(content = content)
        config = speech.RecognitionConfig(
            encoding = 'FLAC',
            language_code="en-IN",
            model="default",
            speech_contexts = custom_vocabulary
            # use_enhanced=True,
            # speech_contexts=[speech.SpeechContext(phrases=custom_vocabulary)],
            
            # sample_rate_hertz=44100,   
        )
        # Detects speech in the audio file
        response = client.recognize(config=config, audio = audio)
        # print(response.results)
        for result in response.results:
            # print("Transcript: {}".format( result.alternatives [0]. transcript))
            return(( result.alternatives [0]. transcript))
    
    
    recorded_audio = record_until_silence()
    save_audio_to_flac(recorded_audio, recorded_file_name) # saving the recorded audio data to a FLAC file
    raw_speech_text = cloud_speech_to_text(recorded_file_name)
    if raw_speech_text != None:
        raw_speech_text = raw_speech_text.lower()
        # os.remove(recorded_file_name)
        print("pre speech: ",raw_speech_text)

#################################################   Transcribing complete #################################
    # if well name is present then combine the single letter words
        from configparser import ConfigParser 
        configuration = ConfigParser() 
        configuration.read('config.ini')
        well_types = configuration.get('well_types','wells')
        well_types = (well_types.split(','))

        raw_speech_list = raw_speech_text.split(" ")
        check = any(item in raw_speech_list for item in well_types)
        if check:
            processed_speech = combine_single_letter_words(raw_speech_text)
            print("processed Speech: ",processed_speech)
        else:
            processed_speech = raw_speech_text

        result_text = find_most_similar_word(processed_speech)
    else:
        result_text = raw_speech_text
     
################### Similarity find for Well Names done ####################
    f = open("stt_out.txt", "w")
    f.write(str(result_text))
    f.close()
    return(result_text)
    
    
    
data = speech_to_text()
print('Final_speech: ',data)

