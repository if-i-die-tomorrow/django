from rest_framework import serializers

from .models import Job, NPC


class JobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class NPCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NPC
        fields = '__all__'
