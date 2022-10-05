from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from .models import *
from .forms import *
from django.db.models import Q

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *


def create_view(request):
    create_form = PostForm()
    
    if request.method == 'POST':
        create_form = PostForm(request.POST, request.FILES)
        
        if create_form.is_valid():
            instance = create_form.save(commit=False)
            instance.author = request.user
            instance.save()
            
            return redirect('blog:home')
    else:
        create_form = PostForm()
        
    context = {
        'create_form' : create_form 
    }
    return render(request, 'blog/create_post.html', context)

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name= 'blog/home.html'
    
    def get_queryset(self):
        search = self.request.GET.get('q', '')
        multiple_search = Q(Q(title__icontains=search) | Q(description__icontains=search))
        posts = Post.objects.filter(multiple_search)
        return posts
    
    

class PostDetails(DetailView):
    model = Post
    template_name='blog/details.html'
    context_object_name = 'detail'
    
    
class postApi(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class postApiDetail(APIView):
    def get_object(self, slug):
        Post.objects.get(slug=slug)
    
    def get(self, request, slug, format=None):
        post = self.get_object(slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
        
    def put(self, request, slug, format=None):
        post = self.get_object(slug)
        serializer = UserProfileSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, slug, forat=None):
        userprofile = self.get_object(slug)
        userprofile.delete 
        return Response(status=status.HTTP_204_NO_CONTENT)
    
