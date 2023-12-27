from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import FormUser

class PageHome(View):
    template_home = 'appSite/index.html'
    def get(self, request):
        return render(request, self.template_home)
    def post(self, request):
        user_name = request.POST['last_name']
        user_email = request.POST['email']
        method = request.POST['method']
        
        if method == 'create':
            user_age = request.POST['age']
            try:
                FormUser.objects.create(
                    name=user_name,
                    email=user_email,
                    age=user_age
                )
            except:
                pass
        elif method == 'update':
            FormUser.objects.filter(
                email=user_email
            ).update(
                name=user_name
            )

        return redirect('urlPageHome')