from django.db import models
from django.utils.translation import gettext_lazy as _

from village.models import NPC


# Create your models here.


class Tag(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    definition = models.TextField(max_length=600)

    def __str__(self):
        return self.code


class Story(models.Model):
    class VisibilityEnum(models.TextChoices):
        PRIVATE = 'PR', _('Private')
        NOT_LISTED = 'NL', _('Not Listed')
        ANONYMOUS = 'AN', _('Anonymous')
        PUBLIC = 'PU', _('Public')

    title = models.CharField(max_length=120)
    synopsis = models.TextField(max_length=600, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    author = models.ManyToManyField(NPC)
    visibility = models.CharField(max_length=2, choices=VisibilityEnum.choices, default=VisibilityEnum.PRIVATE)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=120, blank=True, null=True)
    body = models.TextField()
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    author = models.ManyToManyField(NPC, blank=True)

    def __str__(self):
        return self.title
