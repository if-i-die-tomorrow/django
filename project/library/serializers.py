from rest_framework import serializers

from library.models import Tag, Story, Chapter

from village.serializers import NPCSerializer
from village.models import NPC


class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
