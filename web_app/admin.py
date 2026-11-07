from django.contrib import admin
from web_app.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','subject','created_date','updated_date')
    empty_value_display = '-empty-'
    search_fields = ['name', 'message']
admin.site.register(Contact, ContactAdmin)