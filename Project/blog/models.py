from django.db import models
from Authenticate.models import *
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models import signals
from django.contrib.auth import get_user_model
from django.utils.text import slugify
    
class Post(models.Model):
    post_image = models.ImageField(upload_to='post_images', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length = 800)
    body = RichTextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @receiver(signals.pre_save, sender="blog.Post")
    def populate_slug(sender, instance, **kwargs):
        instance.slug = slugify(instance.title)