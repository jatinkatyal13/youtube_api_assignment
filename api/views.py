from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from api.models import Video


class VideoPagination(PageNumberPagination):
    page_size = 2

class VideoSerializer(serializers.Serializer):
    video_id = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    published_at = serializers.DateTimeField()
    thumbnail_url = serializers.URLField()

class GetVideosView(ListAPIView):
    queryset = Video.objects.order_by("-published_at")
    serializer_class = VideoSerializer
    pagination_class = VideoPagination

class SearchVideosView(ListAPIView):
    queryset = Video.objects.order_by("-published_at")
    serializer_class = VideoSerializer
    pagination_class = VideoPagination
    filter_backends = [SearchFilter]
    search_fields = ['$title', '$description']
