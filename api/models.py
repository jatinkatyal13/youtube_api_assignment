from exapi.youtube.models import YoutubeVideo
from django.db import models


class Video(models.Model):
    video_id = models.CharField(unique=True, max_length=128, primary_key=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnail_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @classmethod
    def from_youtube_video(cls, youtube_video: YoutubeVideo) -> "Video":
        return cls(
            video_id=youtube_video.video_id,
            title=youtube_video.title,
            description=youtube_video.description,
            published_at=youtube_video.published_at,
            thumbnail_url=youtube_video.thumbnail_url,
        )
