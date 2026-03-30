from django.urls import path
from web_app.views import home,about, contact
from django.contrib.sitemaps.views import sitemap
from web_app.sitemaps import StaticViewSitemap
from web_app import views
from blog.sitemaps import BlogSitemap
app_name = 'web_app'

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
}

urlpatterns = [
    path('',home ,name='home'),
    path('about',about ,name='about'),
    path ('contact', contact ,name='contact'),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
