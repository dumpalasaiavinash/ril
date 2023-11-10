# import sounddevice as sd
# import numpy as np
# from scipy.io.wavfile import write

# def record_until_silence(sample_rate=44100, silence_threshold=0.01):
#     print("Recording...")

#     audio_data = []
#     silence_counter = 5

#     def callback(indata, frames, time, status):
#         if status:
#             print(status, flush=True)
#         audio_data.append(indata.copy())
#         if np.max(np.abs(indata)) < silence_threshold:
#             nonlocal silence_counter
#             silence_counter += 1
#         else:
#             silence_counter = 0

#     with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):
#         sd.sleep(1000)  # Give some time for the stream to start
#         while silence_counter < 30:  # Adjust the silence counter threshold based on your needs
#             sd.sleep(100)

#     print("Recording finished.")
#     return np.concatenate(audio_data, axis=0)

# def save_audio_to_wav(audio_data, filename, sample_rate=44100):
#     write(filename, sample_rate, audio_data)

# if __name__ == "__main__":
#     recorded_audio = record_until_silence()

#     # You can save the recorded audio data to a WAV file
#     save_audio_to_wav(recorded_audio, "recorded_audio.wav")






import sounddevice as sd
import numpy as np
import soundfile as sf

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

if __name__ == "__main__":
    recorded_audio = record_until_silence()

    # You can save the recorded audio data to a FLAC file
    save_audio_to_flac(recorded_audio, "recorded_audio.flac")
