# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

import floppyforms.__future__ as forms
from floppyforms.widgets import EmailInput, TextInput

from .models import (ConvidadoRSVP, AcompanhanteRSVP, Convidado,
                     Acompanhante, RSVP, )
from .validators import phone_validator


class ConfirmacaoHomeForm(forms.Form):
    fone = forms.CharField(
        widget=TextInput(attrs={'placeholder': 'Ex: 12 9991 088 998'}),
        label=_("Telefone"), required=True,
        help_text='Se deseja alterar sua confirmação, entre com o mesmo telefone.')
    email = forms.EmailField(
        widget=EmailInput(attrs={'placeholder': 'Ex: camargo@gmail.com'}),
        label=_("E-mail (opcional)"), required=False)

    def __init__(self, *args, **kwargs):
        super(ConfirmacaoHomeForm, self).__init__(*args, **kwargs)
        self.fields['fone'].required = True

    def clean_fone(self):
        fone_validated = phone_validator(self.cleaned_data.get('fone'))
        self.cleaned_data['fone'] = fone_validated
        return self.cleaned_data['fone']


class ConvidadoRSVPForm(forms.ModelForm):

    class Meta:
        model = ConvidadoRSVP
        fields = ('nome_completo', 'rsvp', 'fone', 'email',)
        help_texts = {
            'email': 'Informe um email para enviarmos detalhes da localização e descontos em hoteis.',
        }

    def clean_rsvp(self):
        if self.cleaned_data['rsvp'] == RSVP.vazio:
            raise forms.ValidationError('Responda aqui!!!')
        return self.cleaned_data['rsvp']


class AcompanhanteRSVPForm(forms.ModelForm):

    class Meta:
        model = AcompanhanteRSVP
        fields = ('tipo', 'nome', )
        widgets = {
            'nome': TextInput(
                attrs={'placeholder': 'Entre com o nome do acompanhante', }),
        }


class ListaConvidadoRSVPForm(forms.ModelForm):

    class Meta:
        model = ConvidadoRSVP
        fields = ('contabilizado', )


class ListaConvidadoForm(forms.ModelForm):

    class Meta:
        model = Convidado
        fields = ('rsvp', 'email', 'fone', )


class ListaAcompanhanteForm(forms.ModelForm):

    class Meta:
        model = Acompanhante
        fields = ('rsvp', )
