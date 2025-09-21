import streamlit as st
from utils.ui import require_auth

st.set_page_config(page_title="About")
require_auth()

st.header("About NeuroLearn")
st.markdown(
"""**NeuroLearn** supports diverse learning needs:
- Dyslexia → Text-to-Speech & chunked reading
- ADHD → short, gamified quizzes that encourage focus
- Autism → predictable UI with low-stimulation visuals

Created by Shanmugapriyan & Nandhini
""")
