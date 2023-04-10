import datetime
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
        context["name"] = request.session.get('name')

        # Render index page
        return render(
            request,
            'Train/index.html',
            context
        )


def my_form(request):
    mail = request.POST["ADRESS"]
    quest = request.POST["QUEST"]
    name = request.POST["USERNAME"]

    # send to session data that user entered
    request.session["mail"] = mail
    request.session["quest"] = quest
    request.session["name"] = name

    if request.POST:
        if not(mail and name and quest):
            # Not all field filled error
            messages.error(request, "Not all fileds filled")
            return redirect("/")

        elif not re.match(r"^[a-zA-Z-_.0-9]+@[a-zA-Z-_.0-9]+\.(?=.{2,3}$)[a-z]+", mail):
            # call error message
            messages.error(request, "Invalid email")
            # redirect to index page
            return redirect("/")

        # Message to user his message send successfully
        return HttpResponse(f"Thanks, {name}! The answer will be sent to the mail {mail}. Access Date: {datetime.date.today()}")
