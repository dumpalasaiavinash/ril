def chat(flag):
	import streamlit as st
	from animation import animation
	from speech_to_text import speech_to_text 
	from text_to_speech import text_to_speech
	
	botchat = st.empty()
	with botchat.container():
		animation(1,flag)
		flag = flag + 1
		greetings = "Hi there, What do you want to know about"
		with st.chat_message("BOT"):
			st.write(greetings)
		text_to_speech(greetings)
	botchat.empty()
	with botchat.container():
		animation(0,flag)
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
		animation(1,flag)
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
		animation(0,flag)
		flag = flag + 1
		result = "Sure I will search and fetch you the results"
		with st.chat_message("BOT"):
			st.write(result)