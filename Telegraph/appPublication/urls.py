from django.urls import path
from . import views
urlpatterns = [
    path('', views.PublicationPage.as_view(), name="urlPublicationPage"),
    path('<slug:name>', views.OpenPublicPage.as_view(), name="urlOpenPublicPage"),
]