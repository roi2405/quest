from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, CreateUserSerializer
from .models import User
from rest_framework.response import Response
# Create your views here.
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # mail = serializer.data.get('mail')
            # queryset = User.objects.filter(mail=mail)
            # if queryset.exists():  # there's already a user with that mail.
            #     return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            city = serializer.data.get('city')
            eduction = serializer.data.get('education')
            name = serializer.data.get('name')
            user = User(city=city, education=eduction, name=name)
            user.save()

            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

