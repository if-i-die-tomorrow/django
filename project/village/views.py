from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group

from .serializers import JobsSerializer, NPCSerializer, UserSerializer, GroupSerializer
from .models import Job, NPC


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer
    permission_classes = [permissions.IsAuthenticated]


class NPCViewSet(viewsets.ModelViewSet):
    queryset = NPC.objects.all()
    serializer_class = NPCSerializer
    permission_classes = [permissions.IsAuthenticated]
