# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Fornecedor.contato'
        db.add_column(u'fornecedores_fornecedor', 'contato',
                      self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, blank=True),
                      keep_default=False)


        # Changing field 'Fornecedor.categoria'
        db.alter_column(u'fornecedores_fornecedor', 'categoria', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Deleting field 'Fornecedor.contato'
        db.delete_column(u'fornecedores_fornecedor', 'contato')


        # Changing field 'Fornecedor.categoria'
        db.alter_column(u'fornecedores_fornecedor', 'categoria', self.gf('django.db.models.fields.TextField')())

    models = {
        u'fornecedores.fornecedor': {
            'Meta': {'ordering': "(u'nome',)", 'object_name': 'Fornecedor'},
            'categoria': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'contato': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'blank': 'True'}),
            'fone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'fone2': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'})
        }
    }

    complete_apps = ['fornecedores']