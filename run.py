from youdigest.agents.transcript_fetcher import TranscriptFetcher
from youdigest.agents.summarizer import Summarizer

# 
# https://python.langchain.com/docs/integrations/document_loaders/youtube_transcript/

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    # First, fetch the transcript using the TranscriptFetcher
    fetcher = TranscriptFetcher(lang="en")
    transcript = fetcher.fetch_transcript(youtube_url)
    #print(transcript)
    
    # Then, summarize the transcript using the summarizer
    # Summarize the transcript
    summarizer = Summarizer(model="mistral-tiny", temperature=0.1)
    summary = summarizer.summarize(transcript)
    print(summary)
