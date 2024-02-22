from django.shortcuts import render
from .models import Blog, Comment, Response
from django.contrib.auth.models import User
from django.db.models import Count, Q
from datetime import datetime, timedelta

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    responses = Response.objects.filter(blog=blog)
    return render(request, 'blog_detail.html', {'blog': blog, 'comments': comments, 'responses': responses})

def author_blogs(request, author_id):
    author = User.objects.get(id=author_id)
    blogs = Blog.objects.filter(author=author)
    return render(request, 'author_blogs.html', {'author': author, 'blogs': blogs})

def my_recent_liked_blogs(request):
    user = request.user
    recent_liked_blogs = Response.objects.filter(user=user, like_or_not=True).order_by('-response_date')[:5]
    return render(request, 'recent_liked_blogs.html', {'recent_liked_blogs': recent_liked_blogs})

def my_comment_history(request, blog_id):
    user = request.user
    blog = Blog.objects.get(id=blog_id)
    comment_history = Comment.objects.filter(blog=blog, user=user)
    return render(request, 'comment_history.html', {'blog': blog, 'comment_history': comment_history})

def my_comment_history_author(request, author_id):
    user = request.user
    author = User.objects.get(id=author_id)
    comment_history = Comment.objects.filter(blog__author=author, user=user)
    return render(request, 'comment_history_author.html', {'author': author, 'comment_history': comment_history})

def top_commented_blogs(request, user_id):
    user = User.objects.get(id=user_id)
    top_commented_blogs = Blog.objects.annotate(num_comments=Count('comment')).filter(author=user).order_by('-num_comments')[:5]
    return render(request, 'top_commented_blogs.html', {'user': user, 'top_commented_blogs': top_commented_blogs})

def top_liked_disliked_blogs(request):
    three_days_ago = datetime.now() - timedelta(days=3)
    top_liked_blogs = Blog.objects.annotate(num_likes=Count('response', filter=Q(response__like_or_not=True, response__response_date__gte=three_days_ago))).order_by('-num_likes')[:5]
    top_disliked_blogs = Blog.objects.annotate(num_dislikes=Count('response', filter=Q(response__like_or_not=False, response__response_date__gte=three_days_ago))).order_by('-num_dislikes')[:5]
    return render(request, 'top_liked_disliked_blogs.html', {'top_liked_blogs': top_liked_blogs, 'top_disliked_blogs': top_disliked_blogs})
