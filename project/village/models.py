from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class NPC(models.Model):
    pronouns = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.CharField(max_length=10, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        _tpm = f"{self.title} {self.firstname} {self.lastname}"
        if self.pronouns:
            _tpm += f" ({self.pronouns})"
        return _tpm
