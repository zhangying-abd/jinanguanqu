import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

html_path = Path(__file__).parent / "jinanguanqu.html"
html = html_path.read_text(encoding="utf-8")
components.html(html, height=800, scrolling=True)
