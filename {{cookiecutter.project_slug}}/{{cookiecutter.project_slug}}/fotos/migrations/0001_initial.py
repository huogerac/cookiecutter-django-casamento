# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fotos'
        db.create_table(u'fotos_fotos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128, blank=True)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(default=u'', max_length=100, blank=True)),
        ))
        db.send_create_signal(u'fotos', ['Fotos'])


    def backwards(self, orm):
        # Deleting model 'Fotos'
        db.delete_table(u'fotos_fotos')


    models = {
        u'fotos.fotos': {
            'Meta': {'object_name': 'Fotos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['fotos']