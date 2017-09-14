# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Fornecedor.endereco'
        db.add_column(u'fornecedores_fornecedor', 'endereco',
                      self.gf('django.db.models.fields.TextField')(default=u'', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Fornecedor.endereco'
        db.delete_column(u'fornecedores_fornecedor', 'endereco')


    models = {
        u'fornecedores.fornecedor': {
            'Meta': {'ordering': "(u'nome',)", 'object_name': 'Fornecedor'},
            'categoria': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'contato': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'blank': 'True'}),
            'endereco': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'fone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'fone2': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'notas': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['fornecedores']