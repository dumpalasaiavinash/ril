import speech_recognition as sr
import streamlit as st 
from speech_to_text import speech_to_text
from animation import animation
from text_to_speech import text_to_speech
global flag
flag = 0
trigger_word = "hello"
raw_speech_text = ""
playspeed = 0
global botchat

botchat = st.empty()
with botchat.container():
        animation(playspeed,str(flag))
        print(flag)
        flag = flag + 1
        with st.chat_message("BOT"):
            st.write("say "+ trigger_word + " to initiate a conversation" )



def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listening = st.empty()
        listening.write("Listening.....")
        audio = recognizer.listen(source)
    listening.empty()
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        if "hello" in text.lower():
            botchat.empty()
            chat_function(flag)
            print(flag)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")





def chat_function(flag):
    with botchat.container():
        animation(1,str(flag))
        print(flag)
        greetings = "Hi there, What do you want to know about"
        with st.chat_message("BOT"):
            st.write(greetings)
        text_to_speech(greetings)
    botchat.empty()
    flag = flag + 1
    with botchat.container():
        animation(0,str(flag))
        print(flag)
        greetings = "Hi there, What do you want to know about"
        with st.chat_message("BOT"):
            st.write(greetings)
    # botchat.empty()
    listening = st.empty()
    listening.write("Listening.....")
    userchat = st.empty()
    with userchat.container():
        raw_speech_text = speech_to_text()
        with st.chat_message("USER"):
            st.write(raw_speech_text)
            print(raw_speech_text)
    listening.empty()
    botchat.empty()
    flag = flag + 1
    with botchat.container():
        animation(1,str(flag))
        print(flag)
        if raw_speech_text == "":
            result = "Sorry I didn't get you, Can you repeat again"
        else:
            result = "Sure I will search and fetch you the results"
        with st.chat_message("BOT"):
            st.write(result)
        text_to_speech(result)
    botchat.empty()
    flag = flag + 1
    with botchat.container():
        animation(0,str(flag))
        print(flag)
        result = "Sure I will search and fetch you the results"
        with st.chat_message("BOT"):
            st.write(result)
        flag = flag + 1

print(flag)
# if st.button(label="Click to Speak",):
# 	# chat_function()
#     print("hello world")
while True:
    recognize_speech()