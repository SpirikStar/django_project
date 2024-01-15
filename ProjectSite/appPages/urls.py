from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="url-home"),
    re_path(r'news/?$', views.NewsPage.as_view(), name="url-news"),
    re_path(r'senf/?$', views.SenfPage.as_view(), name="url-senf"),
    re_path(r'contact/?$', views.ContactPage.as_view(), name="url-contact"),
]