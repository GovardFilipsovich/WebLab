import re

import django.contrib.messages as messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views import View


class MainView(View):

    def get(self, request, *args, **kwargs):
        # Create context for data saving
        context = {}

        # Updates data
        context["mail"] = request.session.get('mail')
        context["quest"] = request.session.get('quest')

        # Render index page
        return render(
            request,
            'Train/index.html',
            context
        )


def my_form(request):
    mail = request.POST["ADRESS"]
    quest = request.POST["QUEST"]
    if request.POST:
        if not re.match(r"^[a-zA-Z-_.0-9]+@[a-zA-Z-_.0-9]+\.(?=.{2,3}$)[a-z]+", mail):
            # call error message
            messages.error(request, "Invalid email")

            # send to sessiona data that user enter
            request.session["mail"] = mail
            request.session["quest"] = quest

            # redirect to index page
            return redirect("/")

        # Message to user his message send successfully
        return HttpResponse("Thanks! The answer will be sent to the mail %s" % mail)
