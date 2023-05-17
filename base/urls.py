from django.urls import path

from .views import *

urlpatterns = [

    path('', landing, name = 'home'),
    path('why-us/', why_us, name = 'home'),
    path('questions-and-answers/', qa, name = 'home'),

]