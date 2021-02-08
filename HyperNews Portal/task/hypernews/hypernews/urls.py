"""hypernews URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from news.views import IndexView, NewsContentView, AllNewsView, CreateNewsView
from hypernews.settings import STATIC_URL

urlpatterns = [
    path('', IndexView.as_view()),
    path('news/', AllNewsView.as_view()),
    path('news/create/', CreateNewsView.as_view()),
    re_path('news/(?P<link>[0-9]+)/?', NewsContentView.as_view()),
]

urlpatterns += static(STATIC_URL)
