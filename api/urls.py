from django.urls import path

from api.views import GetVideosView, SearchVideosView


urlpatterns = [
    path("videos/", GetVideosView.as_view()),
    path("videos/search", SearchVideosView.as_view()),
]
