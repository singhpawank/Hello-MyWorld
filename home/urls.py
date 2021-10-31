from django.contrib import admin
from django.urls import path, include
from home import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.index, name="home"),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))

]
