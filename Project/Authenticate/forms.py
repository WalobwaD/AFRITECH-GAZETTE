from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=200, widget = forms.PasswordInput(attrs={'class':'form-control'},))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        help_texts = {
            
            'username' : None
        }
        labels = {
            'username' : ('Username'),
        }
        widgets = {
            
            'username': forms.TextInput(attrs={  
                'placeholder':'username',
                'class': 'username form-control'}),
            'email': forms.TextInput(attrs={
                'placeholder':'email',
                'class': 'email form-control'}),
        }
        
        
       
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ['profile_pic']
        
        help_texts = {
            'profile_pic' : None
        }