from django.db import models

class Article(models.Model):
    title = models.CharField('title', max_length=255)
    content = models.CharField('content', max_length=255)