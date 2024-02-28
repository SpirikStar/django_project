from django.urls import path
from . import views
urlpatterns = [
    path('', views.PublicationPage.as_view(), name="urlPublicationPage")
]