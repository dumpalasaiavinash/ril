def speech_to_text():
    import speech_recognition as sr

    r = sr.Recognizer()
    speech = sr.Microphone(device_index=1)
    with speech as source:    
        audio = r.adjust_for_ambient_noise(source)    
        audio = r.listen(source)
    try:    
        raw_speech_text = r.recognize_google(audio , language = 'en-IN')

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        raw_speech_text = ""   
    return(raw_speech_text)


##################### for testing ########################## 
# import speech_recognition as sr
# from google.cloud import speech_v1p1beta1 as speech

# def speech_to_text():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening... Please speak.")
#         try:
#             # Adjust for ambient noise for better recognition
#             recognizer.adjust_for_ambient_noise(source)

#             # Capture audio from the microphone
#             audio_data = recognizer.listen(source)

#             print("Transcribing...")

#             # Use Google Cloud Speech-to-Text API with custom model for transcription
#             client = speech.SpeechClient()

#             custom_vocabulary = ["wellbore", "rig", "rigmanager", "well"]  # Add your domain-specific words here

#             config = speech.RecognitionConfig(
#                 encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#                 sample_rate_hertz=16000,
#                 language_code="en-US",
#                 speech_contexts=[speech.SpeechContext(phrases=custom_vocabulary)],
#             )

#             audio = speech.RecognitionAudio(content=audio_data.frame_data)

#             # Perform speech recognition with custom vocabulary
#             response = client.recognize(config=config, audio=audio)

#             for result in response.results:
#                 print("Transcript: {}".format(result.alternatives[0].transcript))

#         except sr.WaitTimeoutError:
#             print("No speech detected. Please try again.")
#         except sr.RequestError as e:
#             print("Error with the speech recognition service; {0}".format(e))
#         except sr.UnknownValueError:
#             print("Could not understand the audio. Please try again.")



# if __name__ == "__main__":
#     speech_to_text()
