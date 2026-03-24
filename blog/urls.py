from django.urls import path
from blog.views import blog_home, blog_single, test

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name='blog'),
    path('/<int:id>',blog_single, name='single'),
    path('/test', test, name='test'),
]
