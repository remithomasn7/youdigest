# YouDigest

**YouDigest** is an AI agent designed to summarize YouTube videos or podcast audio into concise, readable summaries.  
It uses OpenAI Whisper (or Faster-Whisper) for transcription and Mistral LLMs via LangChain for natural language summarization.

🚀 Perfect for quickly digesting long videos, interviews, or podcasts.

### Features
- Download and extract audio from YouTube videos (via `yt-dlp`)
- Transcribe audio locally using Whisper or Faster-Whisper
- Generate high-quality summaries using Mistral models (via API)
- Simple CLI or Streamlit interface for interaction

### Tech stack
- Python 3
- LangChain
- Whisper / Faster-Whisper
- Mistral LLMs (via API)
- yt-dlp
- Streamlit (optional)

### Status
🚧 MVP / Prototype – ideal for testing ideas, adaptable for production use later.


## License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.


python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
