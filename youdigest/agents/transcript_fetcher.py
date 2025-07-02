import subprocess
import json
import os
from typing import Optional

class TranscriptFetcher:
    def __init__(self, lang: str = "en"):
        self.lang = lang

    def fetch_transcript(self, youtube_url: str) -> Optional[str]:
        video_id = youtube_url.split("v=")[-1]
        transcript_path = f"{video_id}.{self.lang}.json3"

        # 1. Essaye de récupérer les sous-titres manuels
        cmd_manual = [
            "yt-dlp",
            "--write-subs",
            "--sub-lang", self.lang,
            "--skip-download",
            "--sub-format", "json3",
            "-o", "%(id)s.%(ext)s",
            youtube_url
        ]
        subprocess.run(cmd_manual, check=False)

        # 2. Si pas de sous-titres manuels, essaye les auto
        if not os.path.exists(transcript_path):
            cmd_auto = [
                "yt-dlp",
                "--write-auto-sub",
                "--sub-lang", self.lang,
                "--skip-download",
                "--sub-format", "json3",
                "-o", "%(id)s.%(ext)s",
                youtube_url
            ]
            subprocess.run(cmd_auto, check=False)

        if not os.path.exists(transcript_path):
            return None

        # Charge et concatène le texte du transcript
        with open(transcript_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        segments = [e["segs"][0]["utf8"] for e in data["events"] if "segs" in e]
        transcript = " ".join(segments)

        # Nettoie le fichier temporaire
        os.remove(transcript_path)
        return transcript
