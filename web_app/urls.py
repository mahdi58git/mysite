from django.urls import path
from web_app.views import home,about, contact

app_name = 'web_app'

urlpatterns = [
    path('',home ,name='home'),
    path('about',about ,name='about'),
    path ('contact', contact ,name='contact'),
]
