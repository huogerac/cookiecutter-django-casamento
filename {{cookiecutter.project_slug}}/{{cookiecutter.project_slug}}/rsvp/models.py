# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.crypto import get_random_string
from django.core.urlresolvers import reverse

from model_utils import Choices

RSVP = Choices(('vazio', _(' ? ')),
               ('sim', _('Sim')),
               ('nao', _('Não')), )

TIPO_ACOMPANHANTE = Choices(('adulto', _('Adulto')),
                            ('ate_8', _('Até 8 anos')), )


class ConvidadoRSVP(models.Model):
    slug = models.SlugField(max_length=128,
                            blank=True, default=get_random_string)
    data = models.DateTimeField(_('data'), auto_now_add=True)
    rsvp = models.CharField('Confirma presença?',
                            choices=RSVP, default=RSVP.vazio,
                            max_length=16)
    nome_completo = models.CharField('nome completo', max_length=128)
    email = models.EmailField('e-mail', max_length=128, default='', blank=True)
    fone = models.CharField('fone', max_length=32, default='', blank=True)
    eh_primeiro_acesso = models.BooleanField(default=True)
    contabilizado = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Convidado RSVP")
        verbose_name_plural = _("Convidados (RSVP)")

    def __str__(self):
        return "{0} --> {1}".format(self.nome_completo, self.rsvp)

    def get_absolute_url(self):
        return reverse('rsvp.confirmacao.update',
                       kwargs={'pk': self.id, 'slug': self.slug, })

    @property
    def acompanhate_list(self):
        return AcompanhanteRSVP.objects.filter(convidado_rsvp=self)


class AcompanhanteRSVP(models.Model):
    convidado_rsvp = models.ForeignKey(ConvidadoRSVP,
                                       verbose_name=_('convidado'),
                                       related_name='acompanhantes')
    nome = models.CharField('nome', max_length=128)
    tipo = models.CharField('selecione', choices=TIPO_ACOMPANHANTE,
                            default=TIPO_ACOMPANHANTE.adulto,
                            max_length=16)

    class Meta:
        verbose_name = _("Acompanhante RSVP")
        verbose_name_plural = _("Acompanhantes (RSVP)")
        ordering = ('nome', )

    def __str__(self):
        return self.nome

    @property
    def tipo_verbose(self):
        return TIPO_ACOMPANHANTE[self.tipo]


class Convidado(models.Model):
    GRUPOS = Choices(('Noivo.ParteDaMae', _('Noivo - Parte da Mãe')),
                     ('Noivo.ParteDoPai', _('Noivo - Parte do Pai')),
                     ('Noivo.Amigos', _('Noivo - Amigos')),
                     ('Noiva.ParteDaMae', _('Noiva - Parte da Mãe')),
                     ('Noiva.ParteDoPai', _('Noiva - Parte do Pai')),
                     ('Noiva.Amigos', _('Noiva - Amigos')), )
    grupo = models.CharField('Grupo', default='geral', max_length=32,
                             choices=GRUPOS)
    data = models.DateTimeField(_('data'), auto_now_add=True)
    rsvp = models.CharField('Confirma presença?',
                            choices=RSVP, default=RSVP.vazio,
                            max_length=16)
    nome_completo = models.CharField('nome completo', max_length=128)
    email = models.EmailField('e-mail', max_length=128, default='', blank=True)
    fone = models.CharField('fone', max_length=32, default='', blank=True)

    class Meta:
        verbose_name = _("Lista Convidado")
        verbose_name_plural = _("Lista Convidados")

    def __unicode__(self):
        return "{0} --> {1}".format(self.nome_completo, self.rsvp)

    @property
    def acompanhate_list(self):
        return Acompanhante.objects.filter(convidado=self)

    def get_absolute_url(self):
        return reverse('rsvp.listaconvidado.update', kwargs={'pk': self.id, })

    @property
    def confirmado(self):
        return self.rsvp == RSVP.sim

    @property
    def nao_confirmado(self):
        return self.rsvp == RSVP.nao


class Acompanhante(models.Model):
    convidado = models.ForeignKey(Convidado,
                                  verbose_name=_('convidado'),
                                  related_name='acompanhantes')
    rsvp = models.CharField('Confirma presença?',
                            choices=RSVP, default=RSVP.vazio,
                            max_length=16)
    nome = models.CharField('nome', max_length=128)
    tipo = models.CharField('selecione', choices=TIPO_ACOMPANHANTE,
                            default=TIPO_ACOMPANHANTE.adulto,
                            max_length=16)

    class Meta:
        verbose_name = _("Acompanhante")
        verbose_name_plural = _("Acompanhantes")
        ordering = ('nome', )

    def __unicode__(self):
        return self.nome

    @property
    def tipo_verbose(self):
        return TIPO_ACOMPANHANTE[self.tipo]

    @property
    def confirmado(self):
        return self.rsvp == RSVP.sim

    @property
    def nao_confirmado(self):
        return self.rsvp == RSVP.nao

    @property
    def adulto(self):
        return self.tipo == TIPO_ACOMPANHANTE.adulto
