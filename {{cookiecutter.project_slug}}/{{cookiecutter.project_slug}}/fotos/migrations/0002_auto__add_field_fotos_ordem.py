# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Fotos.ordem'
        db.add_column(u'fotos_fotos', 'ordem',
                      self.gf('django.db.models.fields.IntegerField')(default=1, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Fotos.ordem'
        db.delete_column(u'fotos_fotos', 'ordem')


    models = {
        u'fotos.fotos': {
            'Meta': {'object_name': 'Fotos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'ordem': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['fotos']