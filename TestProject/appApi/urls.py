from django.urls import path
from . import views
urlpatterns = [
    path('', views.ApiHome.as_view(), name="urlApiHome")
]