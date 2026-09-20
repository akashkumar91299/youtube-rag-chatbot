import os
import re
import requests
import streamlit as st


def extract_video_id(youtube_url: str) -> str:
    """Extract the video ID from a YouTube URL."""

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

    if re.fullmatch(r"[a-zA-Z0-9_-]{11}", youtube_url.strip()):
        return youtube_url.strip()

    raise ValueError("Invalid YouTube URL or video ID.")


def fetch_transcript(youtube_url: str) -> str:
    """Fetch YouTube transcript using YTranscript API."""

    video_id = extract_video_id(youtube_url)

    # Get API key from local environment
    api_key = os.getenv("YTRANSCRIPT_API_KEY")

    # Get API key from Streamlit Cloud secrets
    if not api_key:
        try:
            api_key = st.secrets["YTRANSCRIPT_API_KEY"]
        except Exception:
            api_key = None

    if not api_key:
        raise ValueError(
            "YTRANSCRIPT_API_KEY is not configured."
        )

    url = "https://ytranscript.com/api/v1/transcript"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    params = {
        "videoId": video_id,
        "lang": "en"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=30
        )

        if response.status_code != 200:
            raise ValueError(
                f"Transcript API error: "
                f"{response.status_code} - {response.text}"
            )

        data = response.json()

        segments = data.get("segments", [])

        if not segments:
            raise ValueError(
                "No transcript was found for this YouTube video."
            )

        transcript = " ".join(
            segment["text"]
            for segment in segments
            if segment.get("text")
        )

        if not transcript.strip():
            raise ValueError("Transcript is empty.")

        return transcript

    except requests.RequestException as e:
        raise ValueError(
            f"Unable to connect to transcript service: {str(e)}"
        )