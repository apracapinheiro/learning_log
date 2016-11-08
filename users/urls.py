# -*- coding: utf-8 -*-

"""Define padrões de URL para learning_logs"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # pagina de login
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    # pagina de logout
    url(r'^logout/$', views.logout_view, name='logout'),
    # pagina de cadastro de usauio
    url(r'^register/$', views.register, name='register'),
]