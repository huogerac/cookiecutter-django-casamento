# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib import admin

from .models import ConvidadoRSVP, AcompanhanteRSVP, Convidado, Acompanhante


class AcompanhanteRSVPInline(admin.TabularInline):
    model = AcompanhanteRSVP


class ConvidadoRSVPAdmin(admin.ModelAdmin):
    inlines = [
        AcompanhanteRSVPInline,
    ]

admin.site.register(ConvidadoRSVP, ConvidadoRSVPAdmin)


class AcompanhanteInline(admin.TabularInline):
    model = Acompanhante


class ConvidadoAdmin(admin.ModelAdmin):
    inlines = [
        AcompanhanteInline,
    ]

admin.site.register(Convidado, ConvidadoAdmin)
