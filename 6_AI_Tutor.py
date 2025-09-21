import streamlit as st
from utils.ui import require_auth
import openai

st.set_page_config(page_title="AI Tutor")
require_auth()

st.header("AI Tutor — Ask Anything")

st.markdown("Type a question and NeuroLearn will explain it in **simple words**.")

question = st.text_area("Your Question:", "What is photosynthesis?")

mode = st.radio("Explanation Style:", ["Child-friendly", "Detailed"])

if st.button("Get Answer"):
    try:
        # You need to set your OpenAI API key as environment variable: export OPENAI_API_KEY='yourkey'
        openai.api_key = st.secrets.get("OPENAI_API_KEY", None)
        if not openai.api_key:
            st.error("API key not found. Please set OPENAI_API_KEY in Streamlit secrets or environment.")
        else:
            style_prompt = "Explain in very simple, child-friendly words." if mode == "Child-friendly" else "Explain in detail for better understanding."
            prompt = f"{style_prompt}\nQuestion: {question}\nAnswer:"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150,
                temperature=0.6
            )
            st.success(response.choices[0].text.strip())
    except Exception as e:
        st.error(f"Error: {e}")
