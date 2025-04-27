from django.utils import timezone  # Correct import for timezone
from django.shortcuts import render  # type: ignore
from .models import Post


# Create your views here.

def post_list(request):
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})
