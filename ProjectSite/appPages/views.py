from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import ContentBanner, AboutMe, Documents

class HomePage(View):
    def get(self, request):
        data = {
            'banner':ContentBanner.objects.order_by("number"),
            'about_me':AboutMe.objects.first(),
            'documents':Documents.objects.all()
        }
        return render(request, 'appPages/home/index.html', data)