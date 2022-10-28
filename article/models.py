from django.db import models
from django.conf import settings

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField(null=True, blank=True)


def __str__(self):
    return str(self.title)