from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import random
from mimesis import Person
from mimesis.locales import Locale


class ApiHome(View):
    def get(self, request):
        return render(request, 'appApi/index.html')

    def post(self, request):
        action = request.POST['action']
        if action == 'generate-password':
            data = self.generate_password(request)
        elif action == 'generate-email':
            data = self.generate_email(request)
        
        return JsonResponse(data)

    def generate_email(self, request):
        data_email = []
        count_email = request.POST['count_email']
        person = Person(Locale.EN)
        for i in range(int(count_email)):
            mail= person.email()
            data_email.append(mail)
        return {
            'status': 'ok',
            'data_email': data_email
        }

    
    def generate_password(self, request):
        count_password = request.POST['count_password']
        len_password = request.POST['len_password']
        data_chars = 'QWERTYUIOPASDFGHJKLZXCVBNM123456789qwertyuiopasdfghjklzxcvbnm'
        data = []

        for psw in range(int(count_password)):
            password = ''
            for char in range(int(len_password)):
                password += data_chars[random.randint(0, len(data_chars)-1)]
            data.append(password)
        return {
            'status': 'ok',
            'data_password': data
        }
