# Import the openai-whisper package
import whisper

# Define a function to record audio from the microphone
def record_audio():
  # Import the sounddevice and soundfile packages
  import sounddevice as sd
  import soundfile as sf

  # Set the sampling rate and duration
  samplerate = 16000
  duration = 10 # in seconds

  # Record the audio and save it as a wav file
  print("Recording...")
  audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1)
  sd.wait()
  sf.write("audio.wav", audio, samplerate)
  print("Done")

# Define a function to transcribe audio using Whisper
def transcribe_audio():
  # Load the Whisper model
  model = whisper.load_model()

  # Open the audio file and read the data
  with open("audio.wav", "rb") as f:
    data = f.read()

  # Transcribe the audio using Whisper
  transcript = model.transcribe(data)

  # Print the transcript
  print("Transcript:", transcript)

# Define a function to make a speech to text chat function
def speech_to_text_chat():
  # Loop until the user says "bye"
  while True:
    # Record the audio from the user
    record_audio()

    # Transcribe the audio using Whisper
    transcribe_audio()

    # Check if the user said "bye"
    if "bye" in transcript.lower():
      # Break the loop
      break

# Call the speech to text chat function
speech_to_text_chat()
