from youdigest.agents.transcript_fetcher import TranscriptFetcher
from youdigest.agents.summarizer import summarize

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    fetcher = TranscriptFetcher(lang="en")
    import pdb; pdb.set_trace()
    transcript = fetcher.fetch_transcript(youtube_url)
    print(transcript)
    summary = summarize(transcript)

    print(summary)
