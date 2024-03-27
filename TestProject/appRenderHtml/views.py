from django.shortcuts import render
from django.views import View
from appKey.models import Product


class HomePage(View):
    def get(self, request):
        object_product = Product.objects.order_by("-price")
        return render(request, 'appRenderHtml/home/index.html', {
            'products':object_product
        })
