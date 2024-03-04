from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import PubNews
import uuid

class PublicationPage(View):
    def get(self, request):
        return render(request, 'appPublication/views-edit.html')
    def post(self, request):
        name_url = str(uuid.uuid4())[:5]
        get_pub, created = PubNews.objects.get_or_create(
            name_url=name_url,
            defaults={
                "content":request.POST['content']
            }
        )
        if created:
            return JsonResponse({
                "status": "ok",
                "url": get_pub.name_url
            })
        return JsonResponse({
            "status": "Erorr",
        })
        