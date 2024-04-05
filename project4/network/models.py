from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    picture = models.ImageField(null=True, blank=True)
    bio = models.CharField(max_length=280, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    work = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}, {self.username}"

# Posts
class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)

# Replies
class Reply(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    og_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=70)
    timestamp = models.DateTimeField(auto_now_add=True)

# Likes
class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

# Follow
class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')

