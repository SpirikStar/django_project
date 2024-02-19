from django.urls import path
from . import views
urlpatterns = [
    path('', views.PageAuth.as_view(), name="urlPageAuth")
]