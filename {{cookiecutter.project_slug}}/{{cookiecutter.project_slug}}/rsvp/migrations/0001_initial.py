# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ConvidadoRSVP'
        db.create_table(u'rsvp_convidadorsvp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('rsvp', self.gf('django.db.models.fields.CharField')(default=u'sim', max_length=16)),
            ('nome_completo', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('email', self.gf('django.db.models.fields.EmailField')(default=u'', max_length=128, blank=True)),
            ('fone', self.gf('django.db.models.fields.CharField')(default=u'', max_length=32, blank=True)),
        ))
        db.send_create_signal(u'rsvp', ['ConvidadoRSVP'])

        # Adding model 'AcompanhanteRSVP'
        db.create_table(u'rsvp_acompanhantersvp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('convidado_rsvp', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'acompanhantes', to=orm['rsvp.ConvidadoRSVP'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default=u'adulto', max_length=16)),
        ))
        db.send_create_signal(u'rsvp', ['AcompanhanteRSVP'])


    def backwards(self, orm):
        # Deleting model 'ConvidadoRSVP'
        db.delete_table(u'rsvp_convidadorsvp')

        # Deleting model 'AcompanhanteRSVP'
        db.delete_table(u'rsvp_acompanhantersvp')


    models = {
        u'rsvp.acompanhantersvp': {
            'Meta': {'ordering': "(u'nome',)", 'object_name': 'AcompanhanteRSVP'},
            'convidado_rsvp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'acompanhantes'", 'to': u"orm['rsvp.ConvidadoRSVP']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "u'adulto'", 'max_length': '16'})
        },
        u'rsvp.convidadorsvp': {
            'Meta': {'object_name': 'ConvidadoRSVP'},
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'fone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_completo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rsvp': ('django.db.models.fields.CharField', [], {'default': "u'sim'", 'max_length': '16'})
        }
    }

    complete_apps = ['rsvp']