from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.signin,name="login"),
    path('Signup',views.signup,name="signup"),
    path('blogForm',views.blogForm,name='blogForm'),
    path('create',views.create,name="create"),
]
