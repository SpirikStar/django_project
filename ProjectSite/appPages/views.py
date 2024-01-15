from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import News

class HomePage(View):
    def get(self, request):
        data = {
            'block_css':'home',
        }
        return render(request, 'appPages/home/index.html', data)
class NewsPage(View):
    def get(self, request):
        data = {
            'block_css':'news',
            'list_news': News.objects.order_by('-date')
        }
        return render(request, 'appPages/news/index.html', data)
class SenfPage(View):
    def get(self, request):
        data = {
            'header':{
                'block_css':'senf',
            }
        }
        return render(request, 'appPages/senf/index.html', data)
class ContactPage(View):
    def get(self, request):
        data = {
            'block_css':'contact',
        }
        return render(request, 'appPages/contact/index.html', data)