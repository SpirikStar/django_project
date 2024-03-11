from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import PubNews
import uuid
from user_agents import parse
from appAnalytics.models import StaticLink

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

class OpenPublicPage(View):
    def get(self, request, name):
        user_agent = request.META['HTTP_USER_AGENT']
        ua_parsed = parse(user_agent)
        
        print(ua_parsed.os.family, ua_parsed.os.version_string)
        print(ua_parsed.browser)
        print(ua_parsed.device)
        print(ua_parsed.is_bot)
        print(ua_parsed.is_touch_capable)
        print(ua_parsed.is_pc)
        print(ua_parsed.is_mobile)
        print(ua_parsed.is_tablet)
        print(ua_parsed.is_email_client)
        try:
            obj_pub = PubNews.objects.get(name_url=name)
            obj_pub.count += 1
            obj_pub.save()
            StaticLink.objects.create(
                pub_news=obj_pub,
                os=ua_parsed.os.family,
                browser=ua_parsed.browser.family,
                is_bot=ua_parsed.is_bot,
                is_touch_capable=ua_parsed.is_touch_capable,
                type_device='pc' if ua_parsed.is_pc else 'mobile' if ua_parsed.is_mobile else 'tablet'
            )
            return render(
                request, 'appPublication/result.html',
                {
                    'content': obj_pub.content
                }
            )
        except:
            return redirect('urlPublicationPage')