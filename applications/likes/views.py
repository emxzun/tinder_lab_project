from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet


class LikesApiView(APIView):
    @staticmethod
    def post(request):
        return Response('Лайк/Дизлайк', status=200)
