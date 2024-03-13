from django.shortcuts import render, redirect
from django.http import JsonResponse # -> отображать словарь для API
from django.views import View
from .models import Product, PhotosProduct, Category, Subcategory


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

class CategorysPage(View):
    def get(self, request):
        data_sub = Subcategory.objects.all()
        data = {}
        for sub in data_sub:
            if sub.category.title not in data:
                data.update({
                    sub.category.title : {
                        sub.id: sub.title
                    }
                })
            else:
                data[sub.category.title].update({
                    sub.id: sub.title
                })
        return render(request, 'appKey/home/index.html', {'object':data})
    

class ProductPage(View):
    def get(self, request, id):
        sub_category = Subcategory.objects.filter(id=id)
        if sub_category:
            data = {
                'title': sub_category.first().title,
                'cards': Product.objects.filter(subcategory=id).values('title', 'price', 'id', 'currency')
            } 
            return render(request, 'appKey/home/product.html', data)
        else:
            return redirect('urlCategorys')
        
class Search(View):
    def post(self, request):
        name_search = request.POST['search']
        product = list(Product.objects.filter(title__iregex=name_search).values('title', 'id'))
        sub_category = list(Subcategory.objects.filter(title__iregex=name_search).values('title', 'id'))
        return JsonResponse({
            'status':'ok',
            'product': product + sub_category
        })