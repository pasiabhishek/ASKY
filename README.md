# ASKY 🎙️

**A**rtificial **S**olutions for **K**nowledge **Y**ield — a simple voice-controlled desktop assistant written in Python.

ASKY listens for your voice commands, talks back out loud, and can open websites, run searches, and pull quick answers from Wikipedia.

## Features

- 🗣️ **Voice input** — listens through your microphone and converts speech to text with Google's speech recognition
- 🔊 **Voice output** — replies out loud using text-to-speech
- 👋 **Time-aware greeting** — greets you with "Good Morning / Afternoon / Evening / Night" based on the current time
- 📺 **YouTube** — open YouTube or search it directly by voice
- 🔍 **Google** — open Google or search it directly by voice
- 📖 **Wikipedia** — get a quick two-sentence summary of any topic
- 🕒 **Time** — ask ASKY for the current time
- 👋 **Exit commands** — say "bye", "exit", "close", "shutdown", or "done" to quit

## Requirements

- Python **3.14** or higher
- A working microphone
- An internet connection (speech recognition and Wikipedia lookups use online services)
- [PortAudio](http://www.portaudio.com/), required by `PyAudio`, which `speech_recognition` needs to access your microphone:
  - **macOS:** `brew install portaudio`
  - **Ubuntu/Debian:** `sudo apt-get install portaudio19-dev`
  - **Windows:** usually installs via pip without extra steps

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Clone the repository
git clone https://github.com/<your-username>/ASKY.git
cd ASKY

# Install dependencies
uv sync
```

Prefer plain `pip`? You'll also need PyAudio for microphone access:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyaudio
```

## Usage

Run the assistant:

```bash
uv run main.py
```

Or, without uv:

```bash
python main.py
```

ASKY will greet you and start listening. Try commands like:

| Say...                                         | ASKY does...                           |
|-------------------------------------------------|-----------------------------------------|
| "open youtube"                                   | Opens youtube.com                       |
| "search cats on youtube"                         | Searches YouTube for "cats"             |
| "open google"                                    | Opens google.com                        |
| "search python tutorials on google"              | Searches Google for "python tutorials"  |
| "wikipedia albert einstein"                      | Reads a short Wikipedia summary         |
| "what's the time" / "time"                       | Tells you the current time              |
| "bye" / "exit" / "close" / "shutdown" / "done"   | Shuts ASKY down                         |

## Project Structure

```
ASKY/
├── main.py          # Core assistant logic
├── pyproject.toml   # Project metadata and dependencies
├── uv.lock          # Locked dependency versions
└── README.md
```

## How It Works

1. `listen()` captures audio from your microphone and transcribes it using Google's speech recognition API.
2. The transcribed text is matched against a set of simple keyword rules in `main()`.
3. Matching commands trigger helper functions (`open_website`, `search_youtube`, `search_google`, `search_wikipedia`).
4. `talk()` uses `pyttsx3` to speak ASKY's responses out loud.

## Roadmap Ideas

- [ ] Wake-word detection instead of always-on listening
- [ ] More natural language parsing for commands
- [ ] Configurable voice, speed, and language
- [ ] Additional integrations (weather, news, calendar, etc.)

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

No license has been specified yet. Consider adding one (e.g. MIT) if you plan to share or accept contributions.
