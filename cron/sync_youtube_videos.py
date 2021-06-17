import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtube_api.settings")
django.setup()

import asyncio

from youtube_api.config import Config
from api.models import Video
from exapi.youtube.service import get_youtube_exapi
from utils.iterator import id_map


CONNECTION_POOL_SIZE = 25


def sync_videos_for_keyword(keyword: str):
    yt_videos = get_youtube_exapi().search_videos(query=keyword)
    yt_video_ids = list(map(lambda x: x.video_id, yt_videos))
    yt_id_vs_yt_video = id_map(yt_videos, lambda x: x.video_id)

    store_videos = Video.objects.filter(video_id__in=yt_video_ids)
    store_video_ids = map(lambda x: x.video_id, store_videos)

    ids_to_create = list(set(yt_video_ids) - set(store_video_ids))
    ids_to_update = list(set(yt_video_ids).intersection(set(store_video_ids)))

    Video.objects.bulk_create(
        [Video.from_youtube_video(yt_id_vs_yt_video[id]) for id in ids_to_create]
    )
    Video.objects.bulk_update(
        [Video.from_youtube_video(yt_id_vs_yt_video[id]) for id in ids_to_update],
        ["title", "description", "thumbnail_url"],
    )


def main():
    print(f"Synced start")

    for keyword in Config.YOUTUBE_KEYWORDS:
        sync_videos_for_keyword(keyword=keyword)

    print(f"Synced complete")


if __name__ == "__main__":
    main()
