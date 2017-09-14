# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import (FornecedoresListView, )


urlpatterns = patterns('',  # noqa

    url(r'^$',
        FornecedoresListView.as_view(),
        name='fornecedores.lista'),

)
