# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from unicodedata import normalize

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Fotos(models.Model):
    titulo = models.CharField(_('Titulo'), max_length=128, blank=True, default='')
    imagem = models.ImageField(
        _('imagem'), upload_to='fotos/', blank=True, default='')
    ordem = models.IntegerField(blank=True, default=1, null=True)

    class Meta:
        verbose_name = _("Foto")
        verbose_name_plural = _("Fotos")

    def __str__(self):
        return self.titulo
