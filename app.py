import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import re

st.set_page_config(
    page_title="AI DBA Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Read HTML
with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()


def image_to_data_uri(path):
    """Convert local image to base64 so it works inside Streamlit iframe."""
    if not os.path.exists(path):
        return None

    ext = os.path.splitext(path)[1].lower()

    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif": "image/gif",
    }

    mime = mime_types.get(ext, "application/octet-stream")

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")

    return f"data:{mime};base64,{encoded}"


# Embed images directly into HTML
image_files = {
    "assets/logo.png": "assets/logo.png",
    "assets/logo.jpg": "assets/logo.jpg",
    "assets/awr-report.png": "assets/awr-report.png",
}

for html_path, actual_path in image_files.items():

    data_uri = image_to_data_uri(actual_path)

    if data_uri:
        html_content = html_content.replace(
            html_path,
            data_uri
        )


# Render presentation
components.html(
    html_content,
    height=850,
    scrolling=False
)
