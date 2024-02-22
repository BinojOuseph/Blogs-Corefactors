"""
URL configuration for Daily_Blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from user import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('author/<int:author_id>/blogs/', views.author_blogs, name='author_blogs'),
    path('my_recent_liked_blogs/', views.my_recent_liked_blogs, name='my_recent_liked_blogs'),
    path('my_comment_history/<int:blog_id>/', views.my_comment_history, name='my_comment_history'),
    path('my_comment_history_author/<int:author_id>/', views.my_comment_history_author, name='my_comment_history_author'),
    path('top_commented_blogs/<int:user_id>/', views.top_commented_blogs, name='top_commented_blogs'),
    path('top_liked_disliked_blogs/', views.top_liked_disliked_blogs, name='top_liked_disliked_blogs'),
]
