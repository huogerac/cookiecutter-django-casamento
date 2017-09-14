# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IntencaoDePresente'
        db.create_table(u'listapresentes_intencaodepresente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('presente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listapresentes.Presente'])),
            ('nome', self.gf('django.db.models.fields.CharField')(default=u'', max_length=128)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=128)),
            ('banco', self.gf('django.db.models.fields.CharField')(default=u'itau', max_length=16)),
            ('mensagem', self.gf('django.db.models.fields.TextField')(default=u'', blank=True)),
            ('valor', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal(u'listapresentes', ['IntencaoDePresente'])


    def backwards(self, orm):
        # Deleting model 'IntencaoDePresente'
        db.delete_table(u'listapresentes_intencaodepresente')


    models = {
        u'listapresentes.intencaodepresente': {
            'Meta': {'ordering': "(u'-id',)", 'object_name': 'IntencaoDePresente'},
            'banco': ('django.db.models.fields.CharField', [], {'default': "u'itau'", 'max_length': '16'}),
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensagem': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'presente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listapresentes.Presente']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '2'})
        },
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