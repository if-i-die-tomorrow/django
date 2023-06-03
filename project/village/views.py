from django.shortcuts import render
from rest_framework import viewsets, permissions

from .serializers import JobsSerializer, NPCSerializer
from .models import Job, NPC


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer
    permission_classes = [permissions.IsAuthenticated]


class NPCViewSet(viewsets.ModelViewSet):
    queryset = NPC.objects.all()
    serializer_class = NPCSerializer
    permission_classes = [permissions.IsAuthenticated]
