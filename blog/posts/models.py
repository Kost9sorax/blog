from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Comment(models.Model):
    body = models.TextField(blank=False)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

