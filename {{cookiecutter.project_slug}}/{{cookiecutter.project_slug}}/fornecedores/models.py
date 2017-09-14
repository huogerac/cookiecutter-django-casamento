# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Fornecedor(models.Model):
    nome = models.CharField(
        _('Fornecedor'), max_length=128, default='')
    categoria = models.CharField(
        _('Categoria (Buffet, Som etc..)'), blank=True, default='',
        max_length=128)
    contato = models.CharField(
        _('Nome do Contato'), blank=True, default='',
        max_length=128)
    email = models.EmailField(
        _('e-mail'), max_length=128, blank=True)
    fone = models.CharField(
        _('Fone'), max_length=32, default='', blank=True)
    fone2 = models.CharField(
        _('Fone (alternativo)'), max_length=32, default='', blank=True)
    site = models.URLField(
        _('Site'), max_length=256, blank=True)
    notas = models.TextField(
        _('Notas'), blank=True, default='')
    endereco = models.TextField(
        _('Endereço'), blank=True, default='')

    class Meta:
        verbose_name = _("Fornecedor")
        ordering = ('nome', )

    def __str__(self):
        return "{0} ({1})".format(self.nome, self.categoria)
