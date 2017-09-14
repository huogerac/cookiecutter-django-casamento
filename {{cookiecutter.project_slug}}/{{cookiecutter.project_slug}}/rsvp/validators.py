# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

import re

from django.utils.translation import ugettext_lazy as _

import floppyforms.__future__ as forms

FONE_INVALID_MSG1 = _(
    "'%(value)s' não é um telefone válido. Entre com o DDD + Número (ex: 12 9 8627 1122)")
FONE_INVALID_MSG2 = _(
    "'%(value)s' não é um telefone válido. Entre com valores números.")
INVALID_PHONE_CHARS = "()-+"


def remove_invalid_phone_chars(phone_number):
    phone_number = "".join(phone_number.split())
    for digit in INVALID_PHONE_CHARS:
        phone_number = phone_number.replace(digit, "")
    return phone_number


def phone_validator(phone_number):
    """ validate and remove spaces from phone numbers """

    phone_number = remove_invalid_phone_chars(phone_number)

    if len(phone_number) < 10:
        raise forms.ValidationError(FONE_INVALID_MSG1,
                                    params={'value': phone_number})
    pattern = r'[^\d{7,10}]'
    if re.search(pattern, phone_number):
        raise forms.ValidationError(FONE_INVALID_MSG2,
                                    params={'value': phone_number})
    return phone_number
