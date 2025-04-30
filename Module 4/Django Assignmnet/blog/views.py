from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm  # You’ll need to create this form




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.publish()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def create_post(request):
    post = Post(title="New Post", text="Text here")
    post.save()
    post.publish()

from django.shortcuts import get_object_or_404

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('post_list')  # or wherever you want users to go after logging out
