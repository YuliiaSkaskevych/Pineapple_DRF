from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50)
    text = models.TextField(max_length=1500)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-create',)

    def __str__(self):
        return self.heading


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.text
