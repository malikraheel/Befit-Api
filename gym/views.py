from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Profile, Message, Exercise
from .serializers import UserSerializer,  ProfileSerializer, MessageSerializer, ExerciseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from .permissions import IsOwner, IsAdminUserOrReadOnly
from rest_framework import status
from rest_framework import viewsets


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ProfileList(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, format=None):
        if request.user.is_superuser:
            message = Message.objects.all()
            serializer = MessageSerializer(message, many=True)
            return Response(serializer.data)
        return Response("Not show message")

    def post(self, request, format=None):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAdminUserOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Exercise.objects.all()
        else:
            return Exercise.objects.filter(name=user)


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('users', request=request, format=None),
            'profiles': reverse('profiles', request=request, format=None),
            'message': reverse('messages', request=request, format=None),
            'exercise': reverse('exercises', request=request, format=None),

        })
