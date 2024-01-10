from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'home/?$', views.HomePage.as_view(), name="url-home"),
]