from django.urls import path, include
from .views import MainView, my_form

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('home', my_form),
    path('__debug__/', include('debug_toolbar.urls')),
]