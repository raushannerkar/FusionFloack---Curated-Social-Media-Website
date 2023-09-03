from PIL import Image, ImageOps
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    caption = models.CharField(max_length=100)
    content = models.FileField(upload_to='post_media/')
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    topic_choices = (
        ('technology', 'Technology'),
        ('animals', 'Animals'),
        ('automobiles', 'Automobiles'),
        ('humour', 'Humour'),
        ('nature', 'Nature'),
        ('news', 'News'),
        ('money', 'Money'),
        ('entertainment', 'Entertainment'),
        ('motivational', 'Motivational'),
        ('sports', 'Sports'),
        ('art', 'Art'),
        ('clips', 'Clips'),
        ('all','All'),
    )
    topic = models.CharField(max_length=20, choices=topic_choices, default='all')

    def __str__(self):
        return self.caption
    
    def get_absolute_url(self):
        return reverse('posts-home')
    
    def is_liked_by_user(self, user):
        return user in self.likes.all()
