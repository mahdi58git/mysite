from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_home(request,**kwargs):
    posts = Post.objects.filter(status=True)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author') != None:
        posts = posts.filter(author__username=kwargs['author'])
    if kwargs.get('tag_name') != None:
        print(kwargs['tag_name'])
        posts = posts.filter(tags__name__iexact=kwargs['tag_name'])
    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page')
        posts = posts.page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        # posts = posts.page(posts.num_pages)
        posts = posts.page(1)

    context = {'posts': posts}
    return render(request, 'blog-home.html', context)

def blog_single(request, id):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts, pk=id)
    context = {'posts': post}
    return render(request, 'blog-single.html', context)

def cat_in_url(request, cat_name):
    posts = Post.objects.filter(status=True)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog-home.html', context)

def search(request):
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        if s:= request.GET.get("search"):
            posts = posts.filter(content__icontains=s)
    context = {'posts': posts}
    return render(request, 'blog-home.html', context)

def test(request):
    return render(request, 'test.html')
