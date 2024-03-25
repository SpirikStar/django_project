from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="urlHome"),
    path('method-django-post', views.MethodDjangoPost.as_view(), name="urlMethodDjangoPost"),
    path('method-ajax-post', views.MethodAjaxPost.as_view(), name="urlMethodAjaxPost")
]