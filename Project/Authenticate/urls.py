from django.urls import path
from .views import *
app_name = 'Authenticate'
urlpatterns = [
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
   
    
]
