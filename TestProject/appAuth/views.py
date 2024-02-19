from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login


class PageAuth(View):
    def get(self, request):
        print(request.user.is_authenticated)
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
            'status':status
        })
