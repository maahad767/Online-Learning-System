from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Section(models.Model):
    title = models.CharField(max_length=256)


class Content(models.Model):
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL, related_name='contents')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=512)
    body = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

