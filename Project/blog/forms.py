from django import forms 
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['post_image', 'title', 'description', 'body']
        widgets = {
            'post_image' : forms.ClearableFileInput(attrs={'class':'form-control w-50 mx-auto'}),
            'title': forms.TextInput(attrs={'class': 'form-control w-50 mx-auto border-t-0 border-x-0 border-orange-300'}),
            'description': forms.TextInput(attrs={'class': 'form-control mx-auto w-75 border-t-0 border-x-0 border-orange-300'}),
        }
        
        