from django.contrib import admin
from django.urls import path
from first_app.views import *

urlpatterns = [
    path('firstapp/welcome/', view=welcome, name='welcome'),
    path('firstapp/login/', view=login, name='login')
]