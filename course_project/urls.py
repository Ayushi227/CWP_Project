"""course_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',include('grammar_checker.urls'),name='index1'),
    path('index/',include('grammar_checker.urls'),name='index'),
    path('loginpage/',include('grammar_checker.urls'),name='login'),
    path('signup/',include('grammar_checker.urls'),name='signup'),
    path('gram_error/',include('grammar_checker.urls'), name='gram_error'),
    path('dictionary/',include('grammar_checker.urls'), name='dictionary'),
    path('normal_dic/',include('grammar_checker.urls'), name='normal_dic'),
    path('page2/',include('grammar_checker.urls'), name='page2'),
    path('admin/', admin.site.urls),
    path('test/',include('posts.urls'),name='test'),
]