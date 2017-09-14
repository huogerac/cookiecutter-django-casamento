# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import (ConfirmacaoHomeView, ConfirmacaoUpdateView,
                    ConfirmacaoAcompanhanteCreateView,
                    ConfirmacaoAcompanhanteDeleteView,
                    ListaConvidadosListView,
                    ConvidadoRSVPUpdateView,
                    ConvidadoUpdateView, AcompanhanteUpdateView, )


urlpatterns = patterns('',  # noqa

    url(r'^confirmacao/$',
        ConfirmacaoHomeView.as_view(),
        name='rsvp.confirmacaohome'),

    url(r'^confirmacao/update/(?P<pk>\d+)-(?P<slug>[\w-]+)/$',
        ConfirmacaoUpdateView.as_view(),
        name='rsvp.confirmacao.update'),

    url(r'^confirmado/$',
        TemplateView.as_view(template_name="rsvp/confirmado.html"),
        name='rsvp.confirmado'),

    url(r'^confirmacao/acompanhante/create/(?P<convidado_pk>\d+)/$',
        ConfirmacaoAcompanhanteCreateView.as_view(),
        name='rsvp.confirmacao.convidado.create'),

    url(r'^confirmacao/acompanhante/delete/(?P<pk>\d+)/(?P<convidado_pk>\d+)/$',
        ConfirmacaoAcompanhanteDeleteView.as_view(),
        name='rsvp.confirmacao.convidado.delete'),

    # lista admin
    url(r'^lista/convidados/$',
        ListaConvidadosListView.as_view(),
        name='rsvp.lista.convidados.list'),

    url(r'^lista/convidados/rsvp/update/(?P<pk>\d+)/$',
        ConvidadoRSVPUpdateView.as_view(),
        name='rsvp.convidadorsvp.update'),

    url(r'^lista/convidados/update/(?P<pk>\d+)/$',
        ConvidadoUpdateView.as_view(),
        name='rsvp.convidado.update'),

    url(r'^lista/acompanhante/update/(?P<pk>\d+)/$',
        AcompanhanteUpdateView.as_view(),
        name='rsvp.acompanhante.update'),
)
