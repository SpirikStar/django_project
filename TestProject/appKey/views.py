from django.shortcuts import render, redirect
from django.http import JsonResponse # -> отображать словарь для API
from django.views import View
from .models import Product, PhotosProduct, Category


class HomeKey(View):
    def get(self, request):
        data = {
            'product': Product.objects.get(id=1)
        }
        return render(request, 'appKey/product/index.html', data)
    def post(self, request):
        if request.POST['method'] == 'addCategory':
            Category.objects.create(
                title=request.POST['text']
            )
            Category.objects.filter(id=3).update(
                title=request.POST['text']
            )
            Category.objects.filter(id=3).delete()

        return redirect('urlHomeKey')