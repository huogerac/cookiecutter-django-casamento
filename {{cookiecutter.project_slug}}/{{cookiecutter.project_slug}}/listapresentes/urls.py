# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import (PaginaPrincipalListView,
                    IntencaoDePresenteCreateView,
                    IntencaoDePresenteConfirmacaoView)


urlpatterns = patterns('',  # noqa

    url(r'^$',
        PaginaPrincipalListView.as_view(),
        name='listapresentes.home'),

    url(r'^comprar-presente/(?P<pk>\d+)/$',
        IntencaoDePresenteCreateView.as_view(),
        name='listapresentes.intencao.create'),

    url(r'^comprar-presente/confirmacao/(?P<pk>\d+)/$',
        IntencaoDePresenteConfirmacaoView.as_view(),
        name='listapresentes.intencao.confirmacao'),

)
