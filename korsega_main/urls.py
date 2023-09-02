from django.urls import path
from django.urls import include
from . import views
from . import database

urlpatterns = [
    path('signin/',views.Signin),
    path('',views.home),
    path('signin/postsign',database.PostSignin),
]