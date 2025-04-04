# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientRegistrationSerializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken


class ClientRegistrationView(APIView):
    def post(self, request):
        data = request.data.copy()
        data['password_hash'] = make_password(data['password_hash'])  # Хэшируем пароль
        serializer = ClientRegistrationSerializer(data=data)

        if serializer.is_valid():
            client = serializer.save()
            refresh = RefreshToken.for_user(client)  # Генерируем JWT
            return Response({"token": str(refresh.access_token)}, status=status.HTTP_201_CREATED)

        return Response({"errors": serializer.errors.get('password_hash', [])}, status=status.HTTP_400_BAD_REQUEST)