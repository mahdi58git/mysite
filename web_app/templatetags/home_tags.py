from django import template
from blog.models import Post,Category
register = template.Library()
@register.inclusion_tag('web-site-last-posts.html', name='last_posts')
def last_post():
    posts = Post.objects.filter(status=True).order_by('-published_date')[:6]
    return {'posts':posts}