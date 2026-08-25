import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AI DBA Assistant",
    layout="wide"
)

with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

components.html(
    html_content,
    height=600,
    scrolling=True
)
