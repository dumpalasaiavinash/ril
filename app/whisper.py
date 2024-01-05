import whisper
model = whisper.load_model("medium")
result = model.transcribe("recording.mp3")
print(result["text"])


#  whisper recorded_audio_old.flac --model medium --languageio_old.flac --model medium --language English 