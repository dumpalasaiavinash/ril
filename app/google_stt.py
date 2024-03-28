# Import necessary libraries
def speech_to_text():
    import sounddevice as sd
    import numpy as np
    import soundfile as sf
    import os
    from google.cloud import speech
    from domain_specific_words import glossary, wells, terms, crucial_words, alphabets, numbers, additional_terms

    # Set the path to your service account key file for Google Cloud Speech-to-Text API
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_key/reliance-stt-39902e2b2216.json"

    # Define the filename for the recorded audio
    recorded_file_name = "recorded_audio_old.flac"

    # Function to record audio until silence is detected
    def record_until_silence(sample_rate=44100, silence_threshold=0.3):
        print("Recording...")

        audio_data = []  # Initialize list to store recorded audio data
        silence_counter = 5  # Counter to track consecutive frames of silence

        # Callback function to process audio data from the microphone input stream
        def callback(indata, frames, time, status):
            if status:
                print(status, flush=True)
            audio_data.append(indata.copy())  # Append the incoming audio data to the list
            # Check if the maximum absolute amplitude of the audio data falls below the silence threshold
            if np.max(np.abs(indata)) < silence_threshold:
                nonlocal silence_counter  # Access the silence_counter variable from the outer scope
                silence_counter += 1  # Increment the silence counter if silence is detected
            else:
                silence_counter = 0  # Reset the silence counter if audio signal is detected

        # Open a stream to capture audio input from the microphone
        with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):
            sd.sleep(1000)  # Give some time for the stream to start
            # Keep recording until the silence counter reaches a threshold
            while silence_counter < 30:  # Adjust the silence counter threshold based on your needs
                sd.sleep(100)

        print("Recording finished.")
        return np.concatenate(audio_data, axis=0)  # Concatenate recorded audio data into a single array

    # Function to save audio data to a FLAC file
    def save_audio_to_flac(audio_data, filename, sample_rate=44100):
        sf.write(filename, audio_data, sample_rate, format='flac')

    # Function to transcribe audio using Google Cloud Speech-to-Text API
    def cloud_speech_to_text(audio_input):
        # Imports the Google Cloud client library
        print("started Transcription")
        # Instantiates a client for Google Cloud Speech-to-Text API
        client = speech.SpeechClient()

        # Read the audio file
        import io
        audio_file = audio_input
        with io.open(audio_file, 'rb') as f:
            content = f.read()

        # Define custom vocabulary for speech recognition
        custom_vocabulary = [
            {"phrases": crucial_words, "boost": 40},
            {"phrases": terms, "boost": 30},
            {"phrases": alphabets, "boost": 5},
            {"phrases": numbers, "boost": 1},
            {"phrases": glossary, "boost": 10},
            {"phrases": additional_terms, "boost": 5},
        ]

        # Configure speech recognition request
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding='FLAC',
            language_code="en-IN",
            model="default",
            speech_contexts=custom_vocabulary
        )

        # Perform speech recognition
        response = client.recognize(config=config, audio=audio)

        # Print the transcribed text
        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))
            return result.alternatives[0].transcript

    # Record audio until silence is detected
    recorded_audio = record_until_silence()

    # Save recorded audio to a FLAC file
    save_audio_to_flac(recorded_audio, recorded_file_name)

    # Transcribe the recorded audio using Google Cloud Speech-to-Text API
    raw_speech_text = cloud_speech_to_text(recorded_file_name)

    # Perform necessary post-processing on the transcribed text
    if raw_speech_text is not None:
        raw_speech_text = raw_speech_text.lower()
        # Perform additional operations on the transcribed text if needed
        print("pre speech: ", raw_speech_text)

    # Return the transcribed text
    return raw_speech_text

# Call the speech_to_text function and print the final transcribed speech
data = speech_to_text()
print('Final_speech: ', data)
