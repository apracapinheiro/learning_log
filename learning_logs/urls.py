# -*- coding: utf-8 -*-

"""Define padrões de URL para learning_logs"""

from django.conf.urls import url

from . import views

urlpatterns = [
    #pagina Inicial
    url(r'^$', views.index, name='index'),
    # mostra todos os assuntos
    url(r'^topic/$', views.topics, name='topics'),
    # pagina de detalhes para um unico assunto
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # pagina para adicionar um novo assunto
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # pagina para adicionar uma nova entrada
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # pagina para editar uma entrada
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]