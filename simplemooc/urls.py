"""simplemooc URL Configuration

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
from django.contrib import admin
from django.urls import path

import core.views
import courses.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', core.views.home, name='home'), #url home  retorna  home
    path('', core.views.home),      #url vazia retorna  home
    path('admin/', admin.site.urls),
    path('contato/', core.views.contact, name='contact'),
    path('courses/', courses.views.index, name='cursos'),
    path('details/' , courses.views.details, name='details'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)
