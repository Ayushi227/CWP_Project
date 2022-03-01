from posts.forms import PostForm
from posts.models import Post
from django.shortcuts import redirect, render

# Create your views here.

def test(request):
    if request.method == "POST":
        word = PostForm(request.POST)
        if word.is_valid():
            word.save()
            return redirect("test/")
    else:
         word = PostForm()
    return render(request, 'test.html',
                  {"posts" : Post.objects.all(),
                  "num_posts" : Post.objects.count(),
                  "word" : word})