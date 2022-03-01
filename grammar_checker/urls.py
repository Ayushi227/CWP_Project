from os import name
from posts.views import test
from django.urls import path
from django.http import HttpResponse

def fav(request):
    return HttpResponse('pretend-binary-data-here', content_type='image/jpeg')



from grammar_checker.views import dictionary, gohome, gram_error, reset, home,postReset,login, normal_dic, page2,signup,logout,postsignup, postlogin,postquiz

urlpatterns = [
    # path('check',check_sentence,name="grammar_checker"),
    path('',home, name='index1'),
    path('index/',gohome, name='index'),
    path('loginpage/',login, name='login'),
    path('signup/',signup, name='signup'),
    path('postsignup/',postsignup, name='postsignup'),
    path('postquiz/',postquiz, name='postquiz'),
    path('postlogin/',postlogin, name='postlogin'),
    path('gram_error/',gram_error, name='gram_error'),
    path('dictionary/',dictionary, name='dictionary'),
    path('normal_dic/',normal_dic, name='normal_dic'),
    path('page2/',page2, name='page2'),
    path('test/',test, name='test'),
    path('logout/',logout, name='logout'),
    path('reset/',reset, name='reset'),
    path('postReset/',postReset, name='postReset'),
    path('favicon.ico', fav),


]

