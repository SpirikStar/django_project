from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import ContentNews


class PageAuth(View):
    def get(self, request):
        # print(request.user.is_authenticated)
        # try:
        #     ContentNews.objects.get(title='bob-redojkregh')
        # except:
        #     ContentNews.objects.create(title='bob-redojkregh', name_url='ewr-wer')
        get_news, created_news = ContentNews.objects.get_or_create(
            title='bob-redojkregh', 
            name_url='ewr-wer'
        )
        print(request.GET.get('last_name', None))
        print(request.GET.get('name', None))
        print(get_news)
        print(created_news)
        return render(request, 'appAuth/auth/index.html')

    def post(self, request):
        _login = request.POST['login']
        _password = request.POST['password']
        user = authenticate(
            username=_login,
            password=_password
        )
        status = ''
        if user is not None:
            if user.is_active:
                login(request, user)
                status += 'ok'
        else:
            status += "errorNotUser"
        return JsonResponse({
            'status': status
        })


class PageReg(View):
    def get(self, request):
        return render(request, 'appAuth/registration/index.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        login = request.POST['login']
        password = request.POST['password_one']
        status = ''
        try:
            status += 'NoLogin'
            User.objects.get(username=login)
        except:
            status += 'ok'
            User.objects.create(
              first_name=first_name,  
              last_name=last_name,  
              email=email,  
              username=login,
              password=password
            )
        return JsonResponse({
            'status': status
        })
