from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    follows = models.ManyToManyField(User,symmetrical=False, related_name='following', blank=True)
    # Add more fields 
    def add_self_to_follows(self):
        self.follows.add(self.user)
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Tweet(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank= False)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return f'Tweet by {self.user_profile.user.username}: {self.content[:20]}...'