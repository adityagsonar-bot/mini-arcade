from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mini Arcade", page_icon="🎮", layout="centered")

GAMES_DIR = Path(__file__).parent / "games"

# name shown in the menu -> (html file, iframe height in px)
GAMES = {
    "🚆 Rail Runner": ("rail-runner.html", 960),
    "✨ Firefly Trail": ("firefly-snake.html", 860),
}

st.title("🎮 Mini Arcade")

choice = st.radio("Pick a game", list(GAMES), horizontal=True, label_visibility="collapsed")
filename, height = GAMES[choice]

html = (GAMES_DIR / filename).read_text(encoding="utf-8")
components.html(html, height=height, scrolling=True)

st.caption(
    "Tip: click inside the game once so it receives keyboard input. "
    "Rail Runner: move the mouse to change lanes, click or press space to jump, ↓ to slide."
)
