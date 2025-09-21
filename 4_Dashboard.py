import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from utils.ui import require_auth
from utils.db import get_quiz_history

st.set_page_config(page_title="Dashboard")
require_auth()

st.header("Dashboard — Progress")
rows = get_quiz_history(st.session_state.user["id"])
if not rows:
    st.info("No quiz history yet. Complete a quiz to see progress here.")
else:
    df = pd.DataFrame(rows, columns=["score","total","created_at"])
    df["created_at"] = pd.to_datetime(df["created_at"])
    st.dataframe(df, use_container_width=True)
    # Plot scores over time
    fig, ax = plt.subplots()
    ax.plot(df["created_at"], df["score"], marker="o")
    ax.set_xlabel("Attempt time")
    ax.set_ylabel("Score")
    ax.set_title("Quiz Score Over Time")
    st.pyplot(fig)
