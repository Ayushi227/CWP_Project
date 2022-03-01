from posts.views import test
from os import name
from django.urls import path

urlpatterns = [
    path('test/',test, name='test')
]