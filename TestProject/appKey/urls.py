from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeKey.as_view(), name="urlHomeKey")
]