from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404

from .forms import *
from .models import *

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
# Create your views here.
def register(request):
    registered = False
    user_form = UserForm()
    # profile_form = UserProfileForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        #profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid(): #and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            #profile = profile_form.save(commit = False)
            #profile.user = user
            
            # if 'profilepic' in request.FILES:
            #     profile.profilepic = request.FILES['profilepic']
                
            # profile.save()
            
            registered = True
    else:
        user_form = UserForm()
        #profile_form = UserProfileForm()          
        
    context = {
        'user_form' : user_form,
        #'profile_form' : profile_form
    }  
    return render(request, 'Authenticate/register.html', context)

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if  user.is_active:
                login(request, user)
                return redirect('blog:home')
            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE!')
        else:
            return HttpResponse('INVALID CREDENTIALS!')
    else:
        return render(request, 'Authenticate/login.html')
    

@login_required
def user_logout(request):
    logout(request)
    return redirect('blog:home')


class apiList(APIView):
    def get(self, request, format=None):
        userprofiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(userprofiles, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class apiDetails(APIView):
    def get_object(self, pk):
        UserProfile.objects.get(pk=pk)
    
    def get(self, request, pk, format=None):
        userprofile = self.get_object(pk)
        serializer = UserProfileSerializer(userprofile)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        userprofile = self.get_object(pk)
        serializer = UserProfileSerializer(userprofile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, forat=None):
        userprofile = self.get_object(pk)
        userprofile.delete 
        return Response(status=status.HTTP_204_NO_CONTENT)
    