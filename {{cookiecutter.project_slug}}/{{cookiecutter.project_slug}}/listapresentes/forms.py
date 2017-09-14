# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

import floppyforms.__future__ as forms
from floppyforms.widgets import EmailInput, TextInput

from .models import IntencaoDePresente


class IntencaoDePresenteForm(forms.ModelForm):

    class Meta:
        model = IntencaoDePresente
        fields = ('presente', 'nome', 'email', 'banco', 'mensagem', )
        help_texts = {
            'email': 'Informe um email para enviarmos a confirmação.',
        }
