from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to = 'blog/%Y/%m/%d/',default='blog/df.jpg')

    title = models.CharField(max_length=255)
    content = models.TextField()

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # tags
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'id': self.id})