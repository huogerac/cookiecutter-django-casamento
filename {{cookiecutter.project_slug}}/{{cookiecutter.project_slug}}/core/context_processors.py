# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf import settings
from datetime import datetime


def configuracoes_processor(request):

    return {
        'DJ_CASAMENTO_DE_UM_LADO': settings.DJ_CASAMENTO_DE_UM_LADO,
        'DJ_CASAMENTO_DO_OUTRO': settings.DJ_CASAMENTO_DO_OUTRO,
        'DJ_CASAMENTO_DATA': settings.DJ_CASAMENTO_DATA,
        'DJ_CASAMENTO_DATE': settings.DJ_CASAMENTO_DATE,
        'DJ_CASAMENTO_LOCAL': settings.DJ_CASAMENTO_LOCAL,
        'DJ_CASAMENTO_CIDADE': settings.DJ_CASAMENTO_CIDADE,
        'DJ_CASAMENTO_JA_ACONTECEU': settings.DJ_CASAMENTO_JA_ACONTECEU,
        'DJ_CASAMENTO_CASADOS_POR': datetime.now().year - settings.DJ_CASAMENTO_DATE.year,
        'DJ_CASAMENTO_EMAIL_CONTATO': settings.DJ_CASAMENTO_EMAIL_CONTATO,
        'DJ_CASAMENTO_SERVER': settings.DJ_CASAMENTO_SERVER,
        'DJ_CASAMENTO_FONE_CONTATO': settings.DJ_CASAMENTO_FONE_CONTATO,
    }
