from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$', views.login, name = 'login'),
    url('^logout$', views.logout, name = 'logout'),
    url('^dashboard$', views.dashboard, name = 'dashboard'),
]
