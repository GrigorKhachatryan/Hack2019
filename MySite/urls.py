"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
<<<<<<< HEAD
from django.conf.urls import url, include

urlpatterns = [
    url(r'^egor/', include('egor.urls')),
=======

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^grigor/$', include('Grigor.urls')),
>>>>>>> f6b256305959d56495e7bc03859a87e4f834b15a
]
