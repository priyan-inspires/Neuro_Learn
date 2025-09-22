# NeuroLearn — Software Edition (Multipage Streamlit + SQLite)

This is a small, production-lean version of NeuroLearn with:
- Login/Signup (SQLite, password hashing)
- Pages for Dyslexia (TTS), ADHD (quiz), Visual Learning
- Dashboard that saves quiz history per user
- Offline-friendly TTS option (pyttsx3); online TTS with gTTS

## Setup
```bash
# Optional: create virtual env
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Linux-only (for offline TTS)
```bash
sudo apt-get update && sudo apt-get install -y espeak
```

## Run
```bash
streamlit run Home.py
```

## Default Workflow
1) Sign up (email + password) or login.
2) Try TTS (Dyslexia Aid).
3) Take the ADHD Focus Quiz → your score is saved.
4) Open Dashboard → view your history chart.
5) Visual Learning → show low-stimulation visuals.

## Notes
- Database file: `data/neurolearn.db` (auto-created)
- Quiz questions: `data/quizzes.json`
- Assets/images: `data/assets/`


Developed by Shanmugapriyan J & Nandhini R
