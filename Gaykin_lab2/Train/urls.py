from django.urls import path
from .views import MainView, my_form

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('home', my_form),
]