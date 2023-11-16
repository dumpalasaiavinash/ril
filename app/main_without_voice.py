import speech_recognition as sr
import streamlit as st
# from speech_to_text import speech_to_text
from animation import animation
from text_to_speech import text_to_speech
from Cloud_record_and_transcribe import speech_to_text
from recognize_speech import recognize_speech

# st.set_option('server.headless', True)  # Set headless mode to True
# st.serve()
# --server.headless true
# streamlit run .\new_main.py --server.headless true    # command for running

trigger_word = "Hello Raj"
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
            print(assistant_trigerred,"assistant")
    return(assistant_trigerred)


def test_chat():
    global flag
    query = st.chat_input("Write your query ",key=flag)
    flag = flag + 1
    if query:
        st.write(f"User has sent the following query: {query}")
    return(query)

def chat():
    global flag
    botchat = st.empty()
    with botchat.container():
        flag = animation(1,flag)
        flag = flag + 1
        greetings = "Hi there, What do you want to know about"
        with st.chat_message("BOT"):
            st.write(greetings)
        # text_to_speech(greetings)
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
        raw_speech_text = st.chat_input("Write your query ",key=flag)
        flag = flag + 1
        
    if raw_speech_text != None:
        with st.chat_message("USER"):
            st.write(raw_speech_text)
        listening.empty()
        botchat.empty()
        with botchat.container():
            flag = animation(1,flag)
            flag = flag + 1
            if raw_speech_text == "" or raw_speech_text == None:
                result = "Sorry I didn't get you, Can you repeat again"
            else:
                # result = "Sure I will search and fetch you the results"
                # print("I am in midde ese")
                # with st.chat_message("BOT"):
                #     st.write(result)
            # text_to_speech(result)
                botchat.empty()
                with botchat.container():
                    flag = animation(0,flag)
                    flag = flag + 1
                    result = "Sure I will search and fetch you the results"
                    with st.chat_message("BOT"):
                        st.write(result)
                # botchat.empty()
                # userchat.empty()
                print(raw_speech_text)
                return(flag)
    else:
        print("went to else")

    
# while True:
#     is_trigerred = True
#     botchat.empty()
#     if is_trigerred == True:
is_trigerred = True
if is_trigerred == True:
    chat()



