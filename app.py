import streamlit as st
import streamlit.components.v1 as components

# Read the HTML file
with open('index.html', 'r') as file:
    html_content = file.read()

# Render the HTML
components.html(html_content, height=600)
