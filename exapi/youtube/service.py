import requests
from typing import List
from datetime import datetime, timedelta, timezone

from youtube_api.config import Config

from exapi.youtube.models import YoutubeVideo


class YoutubeExapi:
    def __init__(self, api_url: str, api_keys: str):
        self._api_url = api_url
        self._api_keys = api_keys

    def search_videos(self, query: str) -> List[YoutubeVideo]:
        now = datetime.now(timezone.utc)
        published_after_datetime = now - timedelta(days=1)
        published_after = published_after_datetime.astimezone().isoformat()
        params = {
            "part": "snippet,id",
            "q": query,
            "publishedAfter": published_after,
        }

        response = self._retry_search_requests(f"{self._api_url}/youtube/v3/search", params=params)

        dikt = response.json()

        return [YoutubeVideo.from_dict(video) for video in dikt["items"]]
    
    def _retry_search_requests(self, *args, **kwargs):
        params = kwargs.pop("params")
        
        for key in self._api_keys:
            try:
                params["key"] = key
                response = requests.get(*args, params=params, **kwargs)
                return response
            except:
                continue
        


def get_youtube_exapi():
    return YoutubeExapi(
        api_url="https://www.googleapis.com", api_keys=Config.YOUTUBE_API_KEYS
    )
