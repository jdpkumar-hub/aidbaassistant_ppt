import base64
import mimetypes
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AI DBA Assistant — Product Demonstration",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's default page spacing so the presentation sits cleanly
# in the browser, like a presentation canvas.
st.markdown(
    """
    <style>
        .stApp {
            margin: 0 !important;
            padding: 0 !important;
        }
        .stApp > header {
            display: none !important;
        }
        [data-testid="stAppViewContainer"] {
            padding: 0 !important;
        }
        [data-testid="stMain"] {
            padding: 0 !important;
        }
        [data-testid="stMainBlockContainer"] {
            max-width: none !important;
            width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        [data-testid="stVerticalBlock"] {
            gap: 0 !important;
        }
        iframe {
            display: block !important;
            border: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).resolve().parent
HTML_FILE = BASE_DIR / "index.html"

html_content = HTML_FILE.read_text(encoding="utf-8")


def embed_local_image(html: str, relative_path: str) -> str:
    """Embed an image as a data URI so it works inside Streamlit's iframe."""
    image_path = BASE_DIR / relative_path
    if not image_path.exists():
        return html

    mime = mimetypes.guess_type(image_path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    data_uri = f"data:{mime};base64,{encoded}"
    return html.replace(relative_path, data_uri)


# Streamlit components run in an iframe. Relative image URLs such as
# assets/logo.jpg are not reliably resolved there, so embed them directly.
for image in (
    "assets/logo.png",
    "assets/logo.jpg",
    "assets/awr-report.png",
):
    html_content = embed_local_image(html_content, image)

# 700px gives the presentation enough room while avoiding the tall 600/850px
# layouts from the earlier versions. scrolling=False prevents an iframe bar.
components.html(
    html_content,
    height=700,
    scrolling=False,
)
