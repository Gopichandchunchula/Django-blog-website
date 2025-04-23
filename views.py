from django.shortcuts import render, get_object_or_404,redirect
from .models import BlogPost,Comment
from django.http import HttpResponse

def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Comment.objects.create(blog_post=post, content=content)
            return redirect('post_detail', post_id=post.id)

    return render(request, 'post_detail.html', {'post': post, 'comments': comments})