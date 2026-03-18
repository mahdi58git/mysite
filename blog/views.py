from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.http import HttpResponse,JsonResponse
def blog_home(request):
    posts = get_object_or_404(Post,status=True)
    context = {'posts': posts}
    return render(request,'blog-home.html',context)
def blog_single(request):
    return render(request,'blog-single.html')
