from django.urls import path
from blog.views import blog_home, blog_single, search, test

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name='blog'),
    path('/<int:id>',blog_single, name='single'),
    path('/catgories/<str:cat_name>',blog_home,name='catgories'),
    path('/author/<str:author>',blog_home,name='author'),
    path('/search/',search,name='search'),
    path('/test', test, name='test'),
]
