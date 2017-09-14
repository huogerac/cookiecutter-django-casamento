# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Presente'
        db.create_table(u'listapresentes_presente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, blank=True)),
            ('descricao', self.gf('django.db.models.fields.TextField')(default=u'', blank=True)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal(u'listapresentes', ['Presente'])


    def backwards(self, orm):
        # Deleting model 'Presente'
        db.delete_table(u'listapresentes_presente')


    models = {
        u'listapresentes.presente': {
            'Meta': {'ordering': "(u'descricao',)", 'object_name': 'Presente'},
            'descricao': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '2'})
        }
    }

    complete_apps = ['listapresentes']