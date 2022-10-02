from django.db import models
from Authenticate.models import *
from ckeditor.fields import RichTextField
    
class Post(models.Model):
    post_image = models.ImageField(upload_to='post_images', blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length = 800)
    body = RichTextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title