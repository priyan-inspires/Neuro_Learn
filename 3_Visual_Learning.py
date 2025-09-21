import streamlit as st
import os
from utils.ui import require_auth

st.set_page_config(page_title="Visual Learning")
require_auth()

st.header("Visual Learning")
st.write("Predictable, low-stimulation visuals to reduce sensory load.")

img_path = "data/assets/shapes.png"
if os.path.exists(img_path):
    st.image(img_path, caption="Shapes & Colors")
else:
    st.info("Add images under data/assets/ to display here.")
