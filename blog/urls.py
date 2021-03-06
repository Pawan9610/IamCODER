"""IamCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('trending/',views.trending,name='trending'),
    path('blogpost/<int:id>',views.blogpost,name='blogpost'),
    path('search/blogpost/<int:id>',views.blogpost,name='blogpost'),
    path("search/", views.search, name="Search"), 
    path("signup/", views.signup, name="signup"), 
    path("login/", views.handlelogin, name="handlelogin"),
    path("logout/", views.handlelogout, name="handlelogout"),
    path("postComment/", views.postComment, name="postComment"),
]

