import streamlit as st
import os
from gtts import gTTS
from utils.ui import require_auth

st.set_page_config(page_title="Dyslexia Aid (TTS)")
require_auth()

st.header("Dyslexia Aid — Text-to-Speech")
txt = st.text_area("Enter text to read aloud:", "NeuroLearn helps every student learn in their own way.")
engine = st.radio("Choose TTS engine:", ["Online (gTTS)", "Offline (pyttsx3)"])
if st.button("Convert to Speech"):
    path = None
    if engine.startswith("Online"):
        tts = gTTS(txt)
        path = "tts_output.mp3"
        tts.save(path)
    else:
        try:
            import pyttsx3
            e = pyttsx3.init()
            path = "tts_output.wav"
            e.save_to_file(txt, path)
            e.runAndWait()
        except Exception as ex:
            st.error("Offline TTS not available; install 'espeak' (Linux) or use Online.")
            st.code(str(ex))
    if path and os.path.exists(path):
        fmt = "audio/mp3" if path.endswith(".mp3") else "audio/wav"
        st.audio(path, format=fmt)
