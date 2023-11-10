import speech_recognition as sr
from google.cloud import speech_v1p1beta1 as speech

def transcribe_audio():
    import os

    # Set the path to your service account key file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_key/reliance-stt-95d847fb6fc9.json"

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... Please speak.")
        try:
            # Adjust for ambient noise for better recognition
            recognizer.adjust_for_ambient_noise(source)

            # Capture audio from the microphone
            audio_data = recognizer.listen(source)

            print("Transcribing...")

            # Use Google Cloud Speech-to-Text API with custom model for transcription
            client = speech.SpeechClient()

            custom_vocabulary = ["your", "domain", "specific", "words"]  # Add your domain-specific words here

            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code="en-US",
                speech_contexts=[speech.SpeechContext(phrases=custom_vocabulary)],
                model='default',
            )    
            # raw_speech_text = recognizer.recognize_google(audio_data , language = 'en-IN')
            # print(raw_speech_text)


            audio = speech.RecognitionAudio(content=audio_data.frame_data)

            # Perform speech recognition with custom vocabulary
            response = client.recognize(config=config, audio=audio)
            print(response)
            print(response.results)

            for result in response.results:
                print("Transcript: {}".format(result.alternatives[0].transcript))

        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.")
        except sr.RequestError as e:
            print("Error with the speech recognition service; {0}".format(e))
        except sr.UnknownValueError:
            print("Could not understand the audio. Please try again.")


transcribe_audio()


# from google.cloud import speech
# import os
# import io

# #setting Google credential
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']= "gcp_key/reliance-stt-95d847fb6fc9.json"
# client = speech.SpeechClient()
# #the path of your audio file
# file_name = "Recording.m4a"
# with io.open(file_name, "rb") as audio_file:
#     content = audio_file.read()
#     audio = speech.RecognitionAudio(content=content)


# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     enable_automatic_punctuation=True,
#     audio_channel_count=2,
#     sample_rate_hertz=16000,
#     language_code="en-US",
# )

# # Sends the request to google to transcribe the audio
# response = client.recognize(request={"config": config, "audio": audio})
# print(response)
# # Reads the response
# for result in response.results:
#     print("Transcript: {}".format(result.alternatives[0].transcript))