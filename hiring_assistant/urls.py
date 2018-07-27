from django.urls import path
from django.contrib import admin
from assistant.views import index

urlpatterns = [
    path('', index),
]
