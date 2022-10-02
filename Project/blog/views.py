from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from .models import *
from .forms import *


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
    

class PostDetails(DetailView):
    model = Post
    template_name='blog/details.html'
    context_object_name = 'detail'
    