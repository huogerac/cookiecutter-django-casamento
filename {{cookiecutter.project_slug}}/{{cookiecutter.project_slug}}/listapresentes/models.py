# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from model_utils import Choices


@python_2_unicode_compatible
class Presente(models.Model):
    titulo = models.CharField(
        _('Título'), blank=True, max_length=128, default='')
    descricao = models.TextField(
        _('Descrição do presente'), blank=True, default='')
    imagem = models.ImageField(
        _('imagem'), upload_to='presentes', blank=True, default='')
    valor = models.DecimalField(
        _('Valor'), max_digits=12, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = _("Presente")
        ordering = ('valor', )

    def __str__(self):
        return "{0} (R${1})".format(self.titulo, self.valor)


@python_2_unicode_compatible
class IntencaoDePresente(models.Model):
    BANCO = Choices(('bradesco', _('Bradesco')),
                    ('itau', _('Itaú')),
                    ('santander', _('Santander')), )
    data = models.DateTimeField(auto_now_add=True, editable=False)
    presente = models.ForeignKey(Presente, verbose_name=_('presente'))
    nome = models.CharField(_('Seu nome'), default='', max_length=128)
    email = models.EmailField(_('e-mail'), max_length=128)
    banco = models.CharField(_('Transferir para o banco'), choices=BANCO,
                             default=BANCO.itau, max_length=16)
    mensagem = models.TextField(
        _('Mensagem para o casal'), blank=True, default='')
    valor = models.DecimalField(
        _('Valor'), max_digits=12, decimal_places=2, default=0.00)
    pagamento_ok = models.BooleanField(default=False)
    saque_ok = models.BooleanField(default=False)
    agradecimento_ok = models.BooleanField(default=False)
    foto_agradecimento_ok = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Intenção de Presente")
        ordering = ('pagamento_ok', 'banco', 'saque_ok',
                    'agradecimento_ok', '-id', )

    def __str__(self):
        ok = " [OK]" if self.pagamento_ok else " --> [VER CONTA]"
        ok += " [$$$acado] " if self.saque_ok else ""
        ok += " [Tks] " if self.agradecimento_ok else ""
        return "{0} ({1},{2}) - {3}".format(
            self.nome, self.valor, self.banco, ok)

    @property
    def centavos(self):
        return float(str(self.valor-int(self.valor))[1:])
