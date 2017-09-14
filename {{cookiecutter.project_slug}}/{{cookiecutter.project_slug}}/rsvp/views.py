# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.utils import timezone

from braces import views

from .models import (ConvidadoRSVP, AcompanhanteRSVP,
                     Convidado, Acompanhante, RSVP, TIPO_ACOMPANHANTE, )
from .forms import (ConfirmacaoHomeForm, ConvidadoRSVPForm,
                    AcompanhanteRSVPForm, ListaConvidadoRSVPForm,
                    ListaConvidadoForm, ListaAcompanhanteForm, )
from .validators import phone_validator


class ConfirmacaoHomeView(FormView):
    form_class = ConfirmacaoHomeForm
    success_url = "/rsvp/confirmado"
    template_name = "rsvp/confirmacaohome.html"

    def form_valid(self, form):
        fone, email = (form['fone'].data,
                       form['email'].data)

        fone = phone_validator(fone)
        email = email.lower()

        if email and fone:
            convidado = ConvidadoRSVP.objects.filter(email=email.lower(),
                                                     fone=fone)
        else:
            if email and ConvidadoRSVP.objects.filter(
                    email=email.lower()):
                convidado = ConvidadoRSVP.objects.filter(
                    email=email.lower())
            else:
                convidado = ConvidadoRSVP.objects.filter(fone=fone)

        if convidado:
            convidado = convidado[0]
        else:
            if email and fone:
                convidado, _ = ConvidadoRSVP.objects.get_or_create(
                    email=email, fone=fone)
            else:
                convidado, _ = ConvidadoRSVP.objects.get_or_create(
                    fone=fone)

        return HttpResponseRedirect(convidado.get_absolute_url())


class ConfirmacaoUpdateView(UpdateView):
    model = ConvidadoRSVP
    form_class = ConvidadoRSVPForm
    success_url = "/rsvp/confirmado"

    def get_context_data(self, **kwargs):
        context = super(ConfirmacaoUpdateView, self).get_context_data(**kwargs)
        context['acompanhante_form'] = AcompanhanteRSVPForm
        return context

    def form_valid(self, form):
        primeiro_acesso = self.object.eh_primeiro_acesso
        self.object = form.save(commit=False)
        self.object.eh_primeiro_acesso = False
        self.object.fone = phone_validator(self.object.fone)
        self.object.email = self.object.email.lower()
        self.object.data = timezone.now()
        self.object.contabilizado = False
        self.object.save()

        if not primeiro_acesso:
            email_body = 'RSVP de {0} atualizado para {1}.'.format(
                self.object.nome_completo, self.object.rsvp)
            send_mail('Elaine & Roger - RSVP', email_body,
                      'roger@na-inter.net',
                      ['huogerac@gmail.com', 'lan.galvao@gmail.com'],
                      fail_silently=False)
        else:
            return HttpResponseRedirect(self.object.get_absolute_url())
        return super(ConfirmacaoUpdateView, self).form_valid(form)


class ConfirmacaoAcompanhanteCreateView(CreateView):
    model = AcompanhanteRSVP
    form_class = AcompanhanteRSVPForm

    def form_valid(self, form):
        convidado = get_object_or_404(ConvidadoRSVP,
                                      pk=self.kwargs['convidado_pk'])
        self.object = form.save(commit=False)
        self.object.convidado_rsvp = convidado
        self.object.save()
        return HttpResponseRedirect(
            self.object.convidado_rsvp.get_absolute_url())


class ConfirmacaoAcompanhanteDeleteView(DeleteView):
    model = AcompanhanteRSVP
    form_class = AcompanhanteRSVPForm

    def get_success_url(self):
        convidado = get_object_or_404(ConvidadoRSVP,
                                      pk=self.kwargs['convidado_pk'])
        return convidado.get_absolute_url()


class ListaConvidadosListView(views.LoginRequiredMixin,
                              views.StaffuserRequiredMixin, ListView):
    model = Convidado
    paginate_by = '140'
    context_object_name = 'imoveis_list'

    def get_context_data(self, **kwargs):
        context = super(ListaConvidadosListView,
                        self).get_context_data(**kwargs)
        context['rsvp_convidado'] = ConvidadoRSVP.objects.all().order_by('-data')
        for grupo, descricao in Convidado.GRUPOS:
            total_convidados = Convidado.objects.filter(
                grupo=grupo).count()
            total_acompanhantes = Acompanhante.objects.filter(
                convidado__grupo=grupo, tipo=TIPO_ACOMPANHANTE.adulto).count()
            grupo_str = slugify(grupo)
            semrsvp_convidados = Convidado.objects.filter(
                grupo=grupo, rsvp=RSVP.vazio).count()
            semrsvp_acompanhantes = Acompanhante.objects.filter(
                convidado__grupo=grupo, rsvp=RSVP.vazio,
                tipo=TIPO_ACOMPANHANTE.adulto).count()
            semrsvp = 100
            total = (total_convidados + total_acompanhantes)
            if total > 0:
                semrsvp = (semrsvp_convidados + semrsvp_acompanhantes) * 100 / total
            context["semrsvp_{0}".format(grupo_str)] = semrsvp

        confirmado_noivo = Convidado.objects.filter(
                grupo__icontains="Noivo", rsvp=RSVP.sim).count()
        confirmado_noivo += Acompanhante.objects.filter(
                convidado__grupo__icontains="Noivo",
                rsvp=RSVP.sim, tipo=TIPO_ACOMPANHANTE.adulto).count()
        context["confirmado_noivo"] = confirmado_noivo

        confirmado_noiva = Convidado.objects.filter(
                grupo__icontains="Noiva", rsvp=RSVP.sim).count()
        confirmado_noiva += Acompanhante.objects.filter(
                convidado__grupo__icontains="Noiva",
                rsvp=RSVP.sim, tipo=TIPO_ACOMPANHANTE.adulto).count()
        context["confirmado_noiva"] = confirmado_noiva

        total_convidados = Convidado.objects.all().count()
        total_convidados += Acompanhante.objects.filter(
            tipo=TIPO_ACOMPANHANTE.adulto).count()
        context["total_convidados"] = total_convidados

        sem_rsvp = Convidado.objects.filter(rsvp=RSVP.vazio).count()
        sem_rsvp += Acompanhante.objects.filter(
            tipo=TIPO_ACOMPANHANTE.adulto, rsvp=RSVP.vazio).count()
        context["sem_rsvp"] = sem_rsvp

        rsvp_nao = Convidado.objects.filter(rsvp=RSVP.nao).count()
        rsvp_nao += Acompanhante.objects.filter(
            tipo=TIPO_ACOMPANHANTE.adulto, rsvp=RSVP.nao).count()
        context["rsvp_nao"] = rsvp_nao

        rsvp_sim = Convidado.objects.filter(rsvp=RSVP.sim).count()
        rsvp_sim += Acompanhante.objects.filter(
            tipo=TIPO_ACOMPANHANTE.adulto, rsvp=RSVP.sim).count()
        context["rsvp_sim"] = rsvp_sim

        context["novos"] = ConvidadoRSVP.objects.filter(contabilizado=False)
        return context

    def get_queryset(self, **kwargs):
        queryset = Convidado.objects.all()
        return queryset.order_by('-grupo', 'nome_completo')


class ConvidadoRSVPUpdateView(views.LoginRequiredMixin,
                              views.StaffuserRequiredMixin, UpdateView):
    model = ConvidadoRSVP
    form_class = ListaConvidadoRSVPForm
    success_url = reverse_lazy('rsvp.lista.convidados.list')
    template_name = "rsvp/convidado_form.html"


class ConvidadoUpdateView(views.LoginRequiredMixin,
                          views.StaffuserRequiredMixin, UpdateView):
    model = Convidado
    form_class = ListaConvidadoForm
    success_url = reverse_lazy('rsvp.lista.convidados.list')
    template_name = "rsvp/convidado_form.html"


class AcompanhanteUpdateView(views.LoginRequiredMixin,
                             views.StaffuserRequiredMixin, UpdateView):
    model = Acompanhante
    form_class = ListaAcompanhanteForm
    success_url = reverse_lazy('rsvp.lista.convidados.list')
    template_name = "rsvp/convidado_form.html"
