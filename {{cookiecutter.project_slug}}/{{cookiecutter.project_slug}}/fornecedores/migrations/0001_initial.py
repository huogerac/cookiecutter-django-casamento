# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fornecedor'
        db.create_table(u'fornecedores_fornecedor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128)),
            ('categoria', self.gf('django.db.models.fields.TextField')(default=u'', blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=128, blank=True)),
            ('fone', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
            ('fone2', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
        ))
        db.send_create_signal(u'fornecedores', ['Fornecedor'])


    def backwards(self, orm):
        # Deleting model 'Fornecedor'
        db.delete_table(u'fornecedores_fornecedor')


    models = {
        u'fornecedores.fornecedor': {
            'Meta': {'ordering': "(u'nome',)", 'object_name': 'Fornecedor'},
            'categoria': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'blank': 'True'}),
            'fone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            'fone2': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'})
        }
    }

    complete_apps = ['fornecedores']