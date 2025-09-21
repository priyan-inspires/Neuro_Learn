import streamlit as st
import json, os
from utils.ui import require_auth
from utils.db import save_quiz_result

st.set_page_config(page_title="ADHD Focus Quiz")
require_auth()

st.header("ADHD Focus Quiz")
QFILE = "data/quizzes.json"

def load_qs():
    if not os.path.exists(QFILE):
        return []
    with open(QFILE, "r", encoding="utf-8") as f:
        return json.load(f)

if "qn" not in st.session_state:
    st.session_state.qn = 0
    st.session_state.score = 0
    st.session_state.finished = False

qs = load_qs()
if not qs:
    st.warning("No quiz questions found. Add them to data/quizzes.json")
else:
    idx = st.session_state.qn
    if not st.session_state.finished and idx < len(qs):
        q = qs[idx]
        st.write(f"**Q{idx+1}.** {q['q']}")
        choice = st.radio("Choose your answer:", q["options"], key=f"q_{idx}")
        if st.button("Submit", key=f"submit_{idx}"):
            if choice == q["answer"]:
                st.success("Correct! ")
                st.session_state.score += 1
            else:
                st.error(f"Wrong ❌. Correct answer: {q['answer']}")
            st.session_state.qn += 1
    else:
        st.success("Quiz Completed!")
        total = len(qs)
        score = st.session_state.score
        st.write(f"Your Score: **{score}/{total}**")
        if not st.session_state.finished:
            # save once
            save_quiz_result(st.session_state.user["id"], score, total)
            st.session_state.finished = True
            st.toast("Saved to dashboard.", icon="✅")
        if st.button("Reset Quiz"):
            st.session_state.qn = 0
            st.session_state.score = 0
            st.session_state.finished = False
