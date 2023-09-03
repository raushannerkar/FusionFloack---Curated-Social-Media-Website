from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',upload_to='profile_pics')
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    followers_count = models.PositiveIntegerField(default=0)

    def update_followers_count(self):
        self.followers_count = self.followers.count()
        self.save()

    def get_followers_url(self):
        return reverse('followers-list', args=[self.user.username])
    
    def get_followers(self):
        return self.followers.all()
    
    def __str__(self):
        return f'{self.user.username} Profile'
 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.profile_pic.path)

        if img.height >300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)