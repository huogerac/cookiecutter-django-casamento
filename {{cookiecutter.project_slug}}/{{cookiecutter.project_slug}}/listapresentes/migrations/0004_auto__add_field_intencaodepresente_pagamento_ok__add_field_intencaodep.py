# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'IntencaoDePresente.pagamento_ok'
        db.add_column(u'listapresentes_intencaodepresente', 'pagamento_ok',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'IntencaoDePresente.saque_ok'
        db.add_column(u'listapresentes_intencaodepresente', 'saque_ok',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'IntencaoDePresente.agradecimento_ok'
        db.add_column(u'listapresentes_intencaodepresente', 'agradecimento_ok',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'IntencaoDePresente.foto_agradecimento_ok'
        db.add_column(u'listapresentes_intencaodepresente', 'foto_agradecimento_ok',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'IntencaoDePresente.pagamento_ok'
        db.delete_column(u'listapresentes_intencaodepresente', 'pagamento_ok')

        # Deleting field 'IntencaoDePresente.saque_ok'
        db.delete_column(u'listapresentes_intencaodepresente', 'saque_ok')

        # Deleting field 'IntencaoDePresente.agradecimento_ok'
        db.delete_column(u'listapresentes_intencaodepresente', 'agradecimento_ok')

        # Deleting field 'IntencaoDePresente.foto_agradecimento_ok'
        db.delete_column(u'listapresentes_intencaodepresente', 'foto_agradecimento_ok')


    models = {
        u'listapresentes.intencaodepresente': {
            'Meta': {'ordering': "(u'-id',)", 'object_name': 'IntencaoDePresente'},
            'agradecimento_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banco': ('django.db.models.fields.CharField', [], {'default': "u'itau'", 'max_length': '16'}),
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            'foto_agradecimento_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensagem': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128'}),
            'pagamento_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'presente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listapresentes.Presente']"}),
            'saque_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '2'})
        },
        u'listapresentes.presente': {
            'Meta': {'ordering': "(u'valor',)", 'object_name': 'Presente'},
            'descricao': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'default': "u''", 'max_length': '100', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '2'})
        }
    }

    complete_apps = ['listapresentes']