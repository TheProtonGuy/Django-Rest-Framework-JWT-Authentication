from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

@api_view(['GET'])
def Home(request):

    return Response("Hello world")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def MyProtectedRoute(request):

    return Response("You have been granted access to my protected route")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetUserInfo(request):

    user = request.user

    user_serializer = UserSerializer(user)

    return Response(user_serializer.data)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):

        # Proceed with the parent method to handle token generation
        try:
            response = super().post(request, *args, **kwargs)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        

        return response