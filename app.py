import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="我的网页", layout="wide")

html = Path("index.html").read_text(encoding="utf-8")
components.html(html, height=800, scrolling=True)
