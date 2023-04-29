import datetime
import json
import os
import pdb
import re

import django.contrib.messages as messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views import View

# Import module with mail matching
from .myform_mail.myform_mail import match_mail

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
    data = {}
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
        elif not match_mail(mail):
            # call error message
            messages.error(request, "Invalid email")
            # redirect to index page
            return redirect("/")
        elif len(quest) < 3:
            # too short question
            messages.error(request, "Too short question")
            return redirect("/")
        elif not re.search('[a-zA-Z]', quest):
            # don't contains letters
            messages.error(request, "Question must contain letters")
            return redirect("/")

        # Check if file exists
        if os.path.exists('./Train/static/json/data.json') and os.stat("./Train/static/json/data.json").st_size != 0:
            # if so add data to file
            with open('./Train/static/json/data.json', 'r') as json_file:
                data = json.load(json_file)
            with open('./Train/static/json/data.json', 'w') as json_file:
                # Check if mail in dict
                if(mail in data.keys()):
                    if quest not in data[mail]:
                        data[mail].append(quest)
                else:
                    data[mail] = [name, quest]
                json.dump(data, json_file)
        else:
            # else create file
            if not os.path.exists('./Train/static/json/data.json'):
                os.mkdir('./Train/static/json/')
            with open('./Train/static/json/data.json', 'w') as file:
                data[mail] = [name, quest]
                json.dump(data, file)

        # Message to user his message send successfully
        return HttpResponse(f"Thanks, {name}! The answer will be sent to the mail {mail}. Access Date: {datetime.date.today()}")
