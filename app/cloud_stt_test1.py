
# Imports the Google Cloud client library
from google.cloud import speech
import os





# Set the path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_key/reliance-stt-95d847fb6fc9.json"
# Instantiates a client



# ###########mic test
# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration
duration = 5

# Start recorder with the given values 
# of duration and sample frequency
recording = sd.rec(int(duration * freq), 
				samplerate=freq, channels=1)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)

# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)






client = speech.SpeechClient()
# # Load the audio file
# import io
# audio_file = 'male.wav'
# with io.open(audio_file, 'rb') as f:
#     content = f.read()

# The name of the audio file to transcribe
gcs_uri = "gs://cloud-samples-data/speech/VER_video_series/Anu1.wav"
audio =  speech.RecognitionAudio(uri=gcs_uri)
# audio =  speech.RecognitionAudio(content = content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.MP3,
    sample_rate_hertz=44100,
    language_code="en-US",
    model="latest_short",
)
# Detects speech in the audio file
response = client.recognize(config=config, audio = audio)
print(response.results)
for result in response. results:
    print("Transcript: {}".format( result.alternatives [0]. transcript))