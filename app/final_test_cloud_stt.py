# import io
# from google.oauth2 import service_account
# from google.cloud import speech
# client_file = 'gcp_key/reliance-stt-95d847fb6fc9.json'
# credentials = service_account.Credentials.from_service_account_file(client_file)
# client = speech. SpeechClient (credentials=credentials)
# # Load the audio file
# audio_file = 'harvard.wav'
# with io.open(audio_file, 'rb') as f:
#     content = f.read()
#     audio = speech.RecognitionAudio(content=content)
# config = speech.RecognitionConfig(
#     encoding=speech. RecognitionConfig. AudioEncoding. LINEAR16,
#     sample_rate_hertz=44100,
#     language_code='en-US',
#     model='latest_long'
# )

# response = client.recognize(config=config,audio=audio)

# print(response.results)


# Imports the Google Cloud client library
from google.cloud import speech
import os

# Set the path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_key/reliance-stt-95d847fb6fc9.json"
# Instantiates a client
client = speech.SpeechClient()
# # Load the audio file
import io
# audio_file = 'recorded_audio.flac'
# with io.open(audio_file, 'rb') as f:
#     content = f.read()

# The name of the audio file to transcribe
gcs_uri = "gs://cloud-samples-data/speech/VER_video_series/Anu1.wav"
audio =  speech.RecognitionAudio(uri=gcs_uri)
# audio =  speech.RecognitionAudio(content = content)

custom_vocabulary = [
                {
                    "phrases":["well bore"],
                    "boost":20
                },
                {
                    "phrases":["well"],
                    "boost":20
                },
                {
                    "phrases":["rig"],
                    "boost":20
                },
                {
                    "phrases":["name", "is", "ana"],
                    "boost":40
                }
                ]


config = speech.RecognitionConfig(
    language_code="en-IN",
    model="latest_long",
    speech_contexts = custom_vocabulary,
    # sample_rate_hertz=44100,
    # encoding = 'FLAC',
)
# Detects speech in the audio file
response = client.recognize(config=config, audio = audio)
for result in response. results:
    print("Transcript: {}".format( result.alternatives [0]. transcript))