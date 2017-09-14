# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ConvidadoRSVP.contabilizado'
        db.add_column(u'rsvp_convidadorsvp', 'contabilizado',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ConvidadoRSVP.contabilizado'
        db.delete_column(u'rsvp_convidadorsvp', 'contabilizado')


    models = {
        u'rsvp.acompanhante': {
            'Meta': {'ordering': "(u'nome',)", 'object_name': 'Acompanhante'},
            'convidado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'acompanhantes'", 'to': u"orm['rsvp.Convidado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rsvp': ('django.db.models.fields.CharField', [], {'default': "u'vazio'", 'max_length': '16'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "u'adulto'", 'max_length': '16'})
        },
        u'rsvp.acompanhantersvp': {
            'Meta': {'ordering': "(u'nome',)", 'object_name': 'AcompanhanteRSVP'},
            'convidado_rsvp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'acompanhantes'", 'to': u"orm['rsvp.ConvidadoRSVP']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "u'adulto'", 'max_length': '16'})
        },
        u'rsvp.convidado': {
            'Meta': {'object_name': 'Convidado'},
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'fone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'grupo': ('django.db.models.fields.CharField', [], {'default': "u'geral'", 'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_completo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rsvp': ('django.db.models.fields.CharField', [], {'default': "u'vazio'", 'max_length': '16'})
        },
        u'rsvp.convidadorsvp': {
            'Meta': {'object_name': 'ConvidadoRSVP'},
            'contabilizado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'eh_primeiro_acesso': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'fone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_completo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rsvp': ('django.db.models.fields.CharField', [], {'default': "u'vazio'", 'max_length': '16'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u'x2BsMAEtzDq3'", 'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['rsvp']