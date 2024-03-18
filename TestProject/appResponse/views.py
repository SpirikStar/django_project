from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import GenerateNumber
import random

class ResponsePage(View):
    def get(self, request):
        # print(GenerateNumber.objects.count())
        d1 = GenerateNumber.objects.all()
        for item in d1:
            # print(item.number, item.status, item.id)
            # if item.status == True:
            if item.status:
                item.number += random.randint(5, 20)
            else:
                item.number -= random.randint(1, 5)
            item.save()
        
        print(GenerateNumber.objects.order_by('-number'))
        # print(GenerateNumber.objects.filter(number=100).exists())
        d_gt = GenerateNumber.objects.filter(number__gt=100)
        # print("Больше 100:", d_gt)
        d_lt = GenerateNumber.objects.filter(number__lt=400)
        # print("Меньше 100:", d_lt)
        
        data = {}
        data['generate_nums'] = list(GenerateNumber.objects.values('id', 'number'))
        # print(GenerateNumber.objects.values('id', 'number'))
        # print(GenerateNumber.objects.values_list('id', 'number'))
        
        return JsonResponse(data, safe=False)
