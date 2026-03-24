from django import template
from blog.models import Post,Category
register = template.Library()

@register.simple_tag(name='blog')
def helo():
    post = Post.objects.filter(status=True)
    return post
@register.filter
def sni (value):
    return value[:100]
@register.inclusion_tag('single-post.html', name='SinglePost')
def single_post():
    posts = Post.objects.filter(status=True).order_by('-published_date')[:3]
    return {'posts':posts}
@register.inclusion_tag('post_catgories.html', name='post_catgories')
def post_catgories():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    cat_idct = {}
    for name in categories:
        cat_idct[name]= posts.filter(category=name).count()
    return {'catgories':cat_idct}

