import sounddevice as sd
import numpy as np
import soundfile as sf
import os
from google.cloud import speech

# Set the path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_key/reliance-stt-95d847fb6fc9.json"
recorded_file_name = "recorded_audio.flac"

def record_until_silence(sample_rate=44100, silence_threshold=0.01):
    print("Recording...")

    audio_data = []
    silence_counter = 0

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

def speech_to_text(audio_input):
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
                "phrases":"well bore",
                "boost":20
            },
            {
                "phrases":"well",
                "boost":20
            },
             {
                "phrases":"rig",
                "boost":20
            },
             {
                "phrases":"rig manager",
                "boost":20
            }
            ]
    
    # custom_vocabulary = ["well bore", "well", "rig", "rig manager"]  # Add your domain-specific words here
    audio =  speech.RecognitionAudio(content = content)
    config = speech.RecognitionConfig(
        encoding = 'FLAC',
        language_code="en-IN",
        model="telephony",
        # speech_contexts=[speech.SpeechContext(phrases=custom_vocabulary)],
        speech_contexts = custom_vocabulary
        # sample_rate_hertz=44100,   
    )
    # Detects speech in the audio file
    response = client.recognize(config=config, audio = audio)
    print(response.results)
    for result in response. results:
        print("Transcript: {}".format( result.alternatives [0]. transcript))

# recorded_audio = record_until_silence()

# # saving the recorded audio data to a FLAC file
# save_audio_to_flac(recorded_audio, recorded_file_name)
speech_to_text(recorded_file_name)

# os.remove(recorded_file_name)




########################## noram stt ###################
# def speech_to_text():
#     import speech_recognition as sr

#     r = sr.Recognizer()
#     speech = sr.Microphone(device_index=1)
#     with speech as source:    
#         audio = r.adjust_for_ambient_noise(source)    
#         audio = r.listen(source)
#     try:    
#         raw_speech_text = r.recognize_google(audio , language = 'en-IN')

#     except sr.UnknownValueError:
#         print("Speech Recognition could not understand audio")
#         raw_speech_text = ""   
#     return(raw_speech_text)

# print(speech_to_text())


########################### from file #############
# import speech_recognition as sr

# def flac_to_text(flac_file_path):
#     recognizer = sr.Recognizer()

#     # Load the FLAC file
#     with sr.AudioFile(flac_file_path) as audio_file:
#         audio_data = recognizer.record(audio_file)

#         try:
#             # Use the Google Web Speech API for speech recognition
#             text = recognizer.recognize_google(audio_data)
#             return text
#         except sr.UnknownValueError:
#             print("Google Web Speech API could not understand audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Web Speech API; {e}")

# if __name__ == "__main__":
#     flac_file_path = "recorded_audio.flac"
#     result = flac_to_text(flac_file_path)

#     if result:
#         print(f"Text from FLAC file: {result}")
