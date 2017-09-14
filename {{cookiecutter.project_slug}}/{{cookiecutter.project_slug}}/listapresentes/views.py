# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division

from random import randint

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from .models import Presente, IntencaoDePresente
from .forms import IntencaoDePresenteForm


class PaginaPrincipalListView(ListView):
    model = Presente
    paginate_by = '100'
    context_object_name = 'presente_list'


class IntencaoDePresenteCreateView(CreateView):
    model = IntencaoDePresente
    form_class = IntencaoDePresenteForm

    def get_initial(self):
        presente = get_object_or_404(Presente, pk=self.kwargs['pk'])
        initial = {
            'presente': presente,
        }
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        centavos = randint(1, 99) / 100
        self.object.valor += centavos + float(self.object.presente.valor)
        self.object.save()
        url = reverse("listapresentes.intencao.confirmacao",
                      kwargs={'pk': self.object.id})
        email_body = '{0} teve uma intenção de presente {1} ({2}, {3})'.format(
            self.object.nome, self.object.presente, self.object.valor, self.object.banco)

        send_mail('Elaine & Roger - PRESENTE', email_body,
                  'roger@na-inter.net',
                  ['huogerac@gmail.com', 'lan.galvao@gmail.com'],
                  fail_silently=False)

        return HttpResponseRedirect(url)


class IntencaoDePresenteConfirmacaoView(UpdateView):
    model = IntencaoDePresente
    form_class = IntencaoDePresenteForm
    template_name = "listapresentes/intencaodepresente_confirmacao.html"
