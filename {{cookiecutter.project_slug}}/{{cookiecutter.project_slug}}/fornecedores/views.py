# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division

from django.views.generic import ListView

from .models import Fornecedor


class FornecedoresListView(ListView):
    model = Fornecedor
    paginate_by = '100'
