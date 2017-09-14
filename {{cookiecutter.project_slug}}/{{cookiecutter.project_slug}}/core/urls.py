# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from .views import ShowHomeView, SaveTheDateView, ConfirmacaoRedirectView
from .forms import LoginForm


urlpatterns = patterns('',  # noqa

    url(r'^confirmacao/$', ConfirmacaoRedirectView.as_view(),
        name='core.confirmacao'),
    url(r'^confirmacao$',
        ConfirmacaoRedirectView.as_view(),),

    url(r'^$', ShowHomeView.as_view(),
        name='core.showhome'),

    url(r'^save-the-date/$',
        SaveTheDateView.as_view(), name='core.savethedate'),

    url(r'^dicasdehoteis/$',
        TemplateView.as_view(template_name="core/dicasdehoteis.html"),
        name='core.dicasdehoteis'),

    url(r'^apps/$',
        TemplateView.as_view(template_name="core/apps.html"),
        name='core.apps'),

    url(r'^agradecimentopresente/$',
        TemplateView.as_view(template_name="core/agradecimento_presente.html"),
        name='core.agradecimentopresente'),

    url(r'^cerimoniareligiosa/$',
        TemplateView.as_view(template_name="core/cerimoniareligiosa.html"),
        name='core.cerimoniareligiosa'),

    url(r'^salaodebeleza/$',
        TemplateView.as_view(template_name="core/salaodebeleza.html"),
        name='core.salaodebeleza'),

    url(r'^restaurante/$',
        TemplateView.as_view(template_name="core/restaurante.html"),
        name='core.restaurante'),

    url(r'^avisoconfirmacao/$',
        TemplateView.as_view(template_name="core/avisoconfirmacao.html"),
        name='core.avisoconfirmacao'),

    # login
    url(r'^auth/$',
        auth_views.login, {'template_name': 'core/login.html',
                           'authentication_form': LoginForm},
        name='url_login_auth'),

)
