"""hypercar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from tickets.views import WelcomeView, Change, Processing, nextv


urlpatterns = [
    path('menu/', WelcomeView.as_view()),
    path('processing',Processing.as_view()),
    path('next', nextv.as_view()),
re_path(r'get_ticket/(?P<service>(change_oil|inflate_tires|diagnostic))', Change.as_view(), name='ticket')


    # re_path('get_ticket/(?P<service>[^/]*)/?', Change.as_view())
]
