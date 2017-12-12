from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    url(r'^home/$', views.goToHome),
    url(r'^login/$', views.goToLogin),

]
