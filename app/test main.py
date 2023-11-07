import streamlit as st 
from speech_to_text import speech_to_text
from animation import animation
from text_to_speech import text_to_speech
raw_speech_text = ""
playspeed = 0
col1, col2, col3 = st.columns([1,3,1])
with col2:
	with st.container():


		if st.button(label="Click to Speak",):
			animation(playspeed,"key1")

			raw_speech_text =  speech_to_text()
			if (len(raw_speech_text) > 0):
				playspeed = 1
			animation(playspeed,"key2")
			text_to_speech("hello I am Avinash How can I help you")


		st.text(raw_speech_text)


