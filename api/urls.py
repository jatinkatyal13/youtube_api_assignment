from django.urls import path

from api.views import PingView


urlpatterns = [
    path("ping/", PingView.as_view())
]
