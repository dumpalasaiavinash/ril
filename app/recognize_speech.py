def recognize_speech(trigger_word,assistant_trigerred):
    import speech_recognition as sr
    import streamlit as st 
    from chat import chat

    timeout_duration = 5
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listening = st.empty()
        listening.write("Listening.....")
        audio = recognizer.listen(source)
    listening.empty()
    try:
        print("Recognizing...")
        recognizing = st.empty()
        recognizing.write("Recognizing.....")
        recognized_text = recognizer.recognize_google(audio)
        print("You said: " + recognized_text)
        recognizing.empty()

        if trigger_word.lower() in recognized_text.strip().lower():
            print("triggered")
            assistant_trigerred = True
            return(assistant_trigerred)
        else:
            return(assistant_trigerred)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
