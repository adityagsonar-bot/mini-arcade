# Mini Arcade

Two small browser games served through Streamlit:

- **Rail Runner**: a three-lane endless runner. Steer with the mouse, click or press space to jump, press ↓ to slide.
- **Firefly Trail**: a snake-style game. Arrow keys or WASD, space to pause.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub.
2. Go to https://share.streamlit.io and click **Create app**.
3. Choose the repo and branch, set **Main file path** to `app.py`, and deploy.

## Structure

```
app.py                   Streamlit launcher
games/rail-runner.html   Self-contained game
games/firefly-snake.html Self-contained game
requirements.txt
.streamlit/config.toml
```
