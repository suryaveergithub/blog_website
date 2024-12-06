from django.shortcuts import render, get_object_or_404
from .models import Post

# Homepage: List all posts
def homepage(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/index.html', {'posts': posts})

# Post Detail: Show a single post
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_app/post_detail.html', {'post': post})
