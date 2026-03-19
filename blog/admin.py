from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ('title','counted_views' ,'published_date', 'status')
    empty_value_display = '-empty-'
    search_fields = ['title', 'content']
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
