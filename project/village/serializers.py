from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Job, NPC


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class JobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class NPCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NPC
        fields = '__all__'
