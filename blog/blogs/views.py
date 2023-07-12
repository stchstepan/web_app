from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm

def index(request):
    return render(request, 'blogs/index.html')

def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.all()

    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    """Page to new a new blog."""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.owner = request.user
            new_form.save()
            return redirect('blogs:blogs')

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(blog, request.user)

    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog
    check_blog_owner(blog, request.user)

    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

def check_blog_owner(blog, user):
    if blog.owner != user:
        raise Http404