from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class PingView(APIView):
    def get(self, request):
        return Response({"message": "pong"})
