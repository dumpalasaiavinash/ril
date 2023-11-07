import speech_recognition as sr
import streamlit as st
from speech_to_text import speech_to_text
from animation import animation
from text_to_speech import text_to_speech
from recognize_speech import recognize_speech

# st.set_option('server.headless', True)  # Set headless mode to True
# st.serve()
# --server.headless true
# streamlit run .\new_main.py --server.headless true    # command for running

trigger_word = "hello"
assistant_trigerred = False
raw_speech_text = ""
playspeed = 0
global botchat
flag = 1

botchat = st.empty()

def page_initiation(assistant_trigerred):
    global flag
    with botchat.container():
        flag = animation(playspeed,flag)
        with st.chat_message("BOT"):
            st.write("say "+ trigger_word + " to initiate a conversation")
            flag = flag + 1
            assistant_trigerred = recognize_speech(trigger_word,assistant_trigerred)
    return(assistant_trigerred)
        

def chat():
    global flag
    botchat = st.empty()
    with botchat.container():
        flag = animation(1,flag)
        flag = flag + 1
        greetings = "Hi there, What do you want to know about"
        with st.chat_message("BOT"):
            st.write(greetings)
        text_to_speech(greetings)
    botchat.empty()
    with botchat.container():
        flag = animation(0,flag)
        flag = flag + 1
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
    with botchat.container():
        flag = animation(1,flag)
        flag = flag + 1
        if raw_speech_text == "":
            result = "Sorry I didn't get you, Can you repeat again"
        else:
            result = "Sure I will search and fetch you the results"
        with st.chat_message("BOT"):
            st.write(result)
        text_to_speech(result)
    botchat.empty()
    with botchat.container():
        flag = animation(0,flag)
        flag = flag + 1
        result = "Sure I will search and fetch you the results"
        with st.chat_message("BOT"):
            st.write(result)
    botchat.empty()
    userchat.empty()
    return(flag)


    
while True:
    is_trigerred = page_initiation(assistant_trigerred)
    botchat.empty()
    if is_trigerred == True:
        botchat.empty()
        print(chat())

