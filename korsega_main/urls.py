from django.urls import path
from django.urls import include
from . import views
from . import database

urlpatterns = [
    path('signin/',views.Signin),
    path('signup/',views.Signup),
    path('',views.home),
    path('signin/postsign',database.PostSignin),
    path('signup/postSignup',database.PostSignup),
    path('/logout',database.logout,name="log"),
    path('forgotpassword',views.forgot_passsword),
    path('forgotpassword/forgotpassword',database.forgot_password),
]