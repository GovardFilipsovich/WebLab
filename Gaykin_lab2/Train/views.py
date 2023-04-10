from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'Train/index.html'
        )

def my_form(request):
    if request.POST:
        mail = request.POST["ADRESS"]
        return HttpResponse("Thanks! The answer will be sent to the mail %s" % mail)