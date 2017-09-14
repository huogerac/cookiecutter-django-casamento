# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Presente.imagem'
        db.add_column(u'listapresentes_presente', 'imagem',
                      self.gf('django.db.models.fields.files.ImageField')(default=u'', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Presente.imagem'
        db.delete_column(u'listapresentes_presente', 'imagem')


    models = {
        u'listapresentes.presente': {
            'Meta': {'ordering': "(u'descricao',)", 'object_name': 'Presente'},
            'descricao': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '2'})
        }
    }

    complete_apps = ['listapresentes']