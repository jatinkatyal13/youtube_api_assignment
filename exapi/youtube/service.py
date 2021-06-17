import requests
from typing import List
from datetime import datetime, timedelta, timezone

from youtube_api.config import Config

from exapi.youtube.models import YoutubeVideo


class YoutubeExapi:
    def __init__(self, api_url: str, api_key: str):
        self._api_url = api_url
        self._api_key = api_key

    def search_videos(self, query: str) -> List[YoutubeVideo]:
        now = datetime.now(timezone.utc)
        published_after_datetime = now - timedelta(days=1)
        published_after = published_after_datetime.astimezone().isoformat()
        params = {"part": "snippet,id", "key": self._api_key, "q": query, "publishedAfter": published_after}

        response = requests.get(
            f"{self._api_url}/youtube/v3/search", params=params
        )

        dikt = response.json()

        return [YoutubeVideo.from_dikt(video) for video in dikt["items"]]


def get_youtube_exapi():
    return YoutubeExapi(
        api_url="https://www.googleapis.com", api_key=Config.YOUTUBE_API_KEY
    )
