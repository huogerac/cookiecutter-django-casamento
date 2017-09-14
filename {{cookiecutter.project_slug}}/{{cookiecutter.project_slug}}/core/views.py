# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView, RedirectView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from datetime import datetime

from fotos.models import Fotos


class ShowHomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(ShowHomeView, self).get_context_data(**kwargs)

        if settings.DJ_CASAMENTO_MODO_SAVE_THE_DATE:
            self.template_name = "core/home_savethedate.html"

        context['fotos'] = Fotos.objects.all().order_by('ordem')

        return context


class SaveTheDateView(TemplateView):
    template_name = "core/savethedate.html"

    def get_context_data(self, **kwargs):
        to = self.request.GET.get("to") or ""
        context = super(SaveTheDateView, self).get_context_data(**kwargs)
        context['to'] = to
        return context


class ConfirmacaoRedirectView(RedirectView):

    def dispatch(self, request, *args, **kwargs):
        self.url = reverse('rsvp.confirmacaohome')
        return redirect(self.url)
