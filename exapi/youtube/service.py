from aiohttp import ClientSession

from youtube_api.config import Config

from exapi.youtube.models import YoutubeVideo


class YoutubeExapi:
    def __init__(self, api_url: str, api_key: str):
        self._api_url = api_url
        self._api_key = api_key

    async def search_videos(self, session: ClientSession, query: str) -> YoutubeVideo:
        params = {"part": "snippet,id", "key": self._api_key, "q": query}

        async with session.get(
            f"{self._api_url}/youtube/v3/search", params=params
        ) as response:
            dikt = await response.json()

            return [YoutubeVideo.from_dikt(video) for video in dikt["items"]]


def get_youtube_exapi():
    return YoutubeExapi(
        api_url="https://www.googleapis.com", api_key=Config.YOUTUBE_API_KEY
    )
