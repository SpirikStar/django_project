from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class PageHome(View):
    template_home = 'appSite/index.html'
    def get(self, request):
        return render(request, self.template_home)
    def post(self, request):
        return HttpResponse(request.POST['number'])