from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


User = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


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
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    publish = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.text
