from django.shortcuts import render
from django.http import JsonResponse # -> отображать словарь для API
from django.views import View

class HomeKey(View):
    def get(self, request):
        return JsonResponse({
            'status':200
        })
