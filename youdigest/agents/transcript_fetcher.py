import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    RequestBlocked
)

class TranscriptFetcher:
    def __init__(self, lang: str = "en", max_retries: int = 3, retry_delay: float = 2.0):
        self.lang = lang
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def extract_video_id(self, youtube_url: str) -> str:
        """
        Extract the video ID from a YouTube URL.
        """
        if "v=" in youtube_url:
            return youtube_url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in youtube_url:
            return youtube_url.split("youtu.be/")[1].split("?")[0]
        else:
            raise ValueError("URL YouTube invalide")

    def fetch_transcript(self, youtube_url: str) -> str:
        try:
            video_id = self.extract_video_id(youtube_url)
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            try:
                # Priorité : transcript manuel
                transcript = transcript_list.find_manually_created_transcript([self.lang])
            except NoTranscriptFound:
                try:
                    # Sinon transcript généré
                    transcript = transcript_list.find_transcript([self.lang])
                except NoTranscriptFound:
                    # Sinon traduire depuis une autre langue
                    transcript = transcript_list.find_transcript(['en', 'fr', 'de']).translate(self.lang)

            segments = self._fetch_with_retries(transcript)
            return self._segments_to_text(segments)

        except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
            return f"[Transcript indisponible] {e}"
        except RequestBlocked:
            return "[Trop de requêtes] Attends un peu ou change d'IP."
        except Exception as e:
            return f"[Erreur inattendue] {e}"

    def _fetch_with_retries(self, transcript) -> list:
        for attempt in range(self.max_retries):
            try:
                return transcript.fetch()
            except Exception as e:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    raise Exception(f"Échec fetch après {self.max_retries} tentatives : {e}")

    def _segments_to_text(self, segments: list) -> str:
        return " ".join(segment.text for segment in segments)



#def extract_video_id(youtube_url: str) -> str:
#    """
#    Extrait l'identifiant de vidéo à partir d'une URL YouTube.
#    """
#    query = urlparse(youtube_url)
#    if query.hostname == 'youtu.be':
#        return query.path[1:]
#    if query.hostname in ('www.youtube.com', 'youtube.com'):
#        if query.path == '/watch':
#            return parse_qs(query.query).get('v', [None])[0]
#        if query.path.startswith('/embed/'):
#            return query.path.split('/')[2]
#        if query.path.startswith('/v/'):
#            return query.path.split('/')[2]
#    raise ValueError("URL YouTube non reconnue")