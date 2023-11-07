import streamlit as st 
from speech_to_text import speech_to_text
from animation import animation
from text_to_speech import text_to_speech
raw_speech_text = ""
playspeed = 0

def chat_function():
	botchat = st.empty()
	with botchat.container():
		animation(1,"key1")
		greetings = "Hi there, What do you want to know about"
		with st.chat_message("BOT"):
			st.write(greetings)
		text_to_speech(greetings)
	botchat.empty()
	with botchat.container():
		animation(0,"key2")
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
		animation(1,"key3")
		if raw_speech_text == "":
			result = "Sorry I didn't get you, Can you repeat again"
		else:
			result = "Sure I will search and fetch you the results"
		with st.chat_message("BOT"):
			st.write(result)
		text_to_speech(result)
	botchat.empty()
	with botchat.container():
		animation(0,"key4")
		result = "Sure I will search and fetch you the results"
		with st.chat_message("BOT"):
			st.write(result)


if st.button(label="Click to Speak",):
	chat_function()


# with st.container():
	
# 	animation(1,"key1")
# 	greetings = "Hi there, What do you want to know about"
# 	text_to_speech(greetings)

# 	raw_speech_text =  speech_to_text()
# 	# prompt = st.chat_input("Say something")
# 	# if prompt:
# 	# 	st.write(f"User has sent the following prompt: {raw_speech_text}")
# 	st.empty()
# 	with st.chat_message("user"):
# 		st.write(raw_speech_text)

# 	# if st.button(label="Click to Speak",):
# 	# 	animation(playspeed,"key1")

# 		# raw_speech_text =  speech_to_text()
# 		if (len(raw_speech_text) > 0):
# 			playspeed = 1
# 		animation(playspeed,"key2")
# 		text_to_speech("hello I am Avinash How can I help you")


# 	st.text(raw_speech_text)


