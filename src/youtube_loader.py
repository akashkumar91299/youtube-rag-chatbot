import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
)


def extract_video_id(youtube_url: str) -> str: # extracting the video id from url
    
    patterns = [
        r"(?:v=)([a-zA-Z0-9_-]{11})",
        r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})",
        r"(?:youtube\.com/shorts/)([a-zA-Z0-9_-]{11})",
        r"(?:youtube\.com/embed/)([a-zA-Z0-9_-]{11})",
    ]

    for pattern in patterns:
        match = re.search(pattern, youtube_url)

        if match:
            return match.group(1)

    # Also allow user to directly enter video ID
    if re.fullmatch(r"[a-zA-Z0-9_-]{11}", youtube_url.strip()):
        return youtube_url.strip()

    raise ValueError("Invalid YouTube URL or video ID.")


def fetch_transcript(youtube_url: str) -> str: # fetch the video transcript
    
    video_id = extract_video_id(youtube_url)

    try:
        transcript_list = YouTubeTranscriptApi().fetch(video_id,languages=['en','hi']).to_raw_data()

        transcript = " ".join( chunk["text"]for chunk in transcript_list)

        if not transcript.strip():
            raise ValueError("Transcript is empty.")

        return transcript

    except TranscriptsDisabled:
        raise ValueError(
            "Transcripts are disabled for this YouTube video."
        )

    except NoTranscriptFound:
        raise ValueError(
            "No transcript was found for this YouTube video."
        )

    except Exception as e:
        raise ValueError(
            f"Unable to fetch transcript: {str(e)}"
        )