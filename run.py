from youdigest.agents.transcript_fetcher import TranscriptFetcher
from youdigest.agents.summarizer import summarize

# 
# https://python.langchain.com/docs/integrations/document_loaders/youtube_transcript/
from langchain_community.document_loaders import YoutubeLoader

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    # First, fetch the transcript using the TranscriptFetcher
    fetcher = TranscriptFetcher(lang="en")
    transcript = fetcher.fetch_transcript(youtube_url)
    #print(transcript)
    
    # Then, summarize the transcript using the summarizer
    summary = summarize(transcript)
    print(summary)
