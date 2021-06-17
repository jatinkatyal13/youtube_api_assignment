from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class YoutubeVideo:
    video_id: str
    title: str
    description: str
    published_at: datetime
    thumbnail: str

    @classmethod
    def from_dikt(cls, dikt) -> "YoutubeVideo":
        return cls(
            video_id=dikt["id"]["videoId"],
            title=dikt["snippet"]["title"],
            description=dikt["snippet"]["description"],
            published_at=dikt["snippet"]["publishedAt"],
            thumbnail=dikt["snippet"]["thumbnails"]["default"]["url"],
        )
