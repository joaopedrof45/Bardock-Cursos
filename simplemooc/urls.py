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


from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

import accounts.views
import core.views
import courses.views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home/', core.views.home, name='home'), #url home  retorna  home
    path('dashboard/', accounts.views.dashboard, name='dashboard'), #url home  retorna  home
    path('', core.views.home),      #url vazia retorna  home
    path('admin/', admin.site.urls),
    path('contato/', core.views.contact, name='contact'),
    path('courses/', courses.views.index, name='cursos'),
    path('details/' , courses.views.details, name='details'),
    path('register/' , accounts.views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        extra_context={'titulo': 'Autenticação'}
    ), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name="logout"),
    path('editar-conta/', accounts.views.edit, name="editar_conta"),
    path('editar-senha/', accounts.views.edit_password, name="editar_senha"),
    path('password_reset/', accounts.views.password_reset, name="password_reset"),
    path(r'confirmar-nova-senha/<key>', accounts.views.password_reset_confirm, name='password_reset_confirm'),
    path('inscricao/', courses.views.enrollment, name="enrollment"),

    #o correto seria ^(?P<slug>[\w_-]+)/$ ao final , mas a epxressao regular nao esta sendo reconhecida
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)
