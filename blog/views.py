from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.http import HttpResponse,JsonResponse
def blog_home(request):

    posts = Post.objects.filter(status=True)
    context = {'posts': posts}
    return render(request,'blog-home.html',context)
def blog_single(request, id):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts,pk=id)
    context = {'posts':post}
    return render(request, 'blog-single.html',context)

def test (request):
    return render(request, 'test.html')