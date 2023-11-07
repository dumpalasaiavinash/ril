def text_to_speech(output_text):
    import pyttsx3

    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 0.9)
    # engine.setProperty('pitch', 0.8)  # Sets the pitch to 0.8
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(output_text) 
    # engine.say('<pitch middle="10">,output_text') 
    engine.runAndWait()
