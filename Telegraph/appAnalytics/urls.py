from django.urls import path
from . import views
urlpatterns = [
    path('<slug:name_link>', views.StaticLinkPage.as_view(), name="urlStaticLinkPage")
]