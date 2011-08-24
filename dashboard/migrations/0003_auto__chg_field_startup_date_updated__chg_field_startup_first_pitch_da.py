# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Startup.date_updated'
        db.alter_column('dashboard_startup', 'date_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, null=True))

        # Changing field 'Startup.first_pitch_date'
        db.alter_column('dashboard_startup', 'first_pitch_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Startup.date_added'
        db.alter_column('dashboard_startup', 'date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True))

        # Changing field 'Startup.first_contact_date'
        db.alter_column('dashboard_startup', 'first_contact_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Person.date_updated'
        db.alter_column('dashboard_person', 'date_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, null=True))

        # Changing field 'Person.date_added'
        db.alter_column('dashboard_person', 'date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True))

        # Changing field 'Review.date'
        db.alter_column('dashboard_review', 'date', self.gf('django.db.models.fields.DateField')(auto_now=True, null=True))


    def backwards(self, orm):
        
        # Changing field 'Startup.date_updated'
        db.alter_column('dashboard_startup', 'date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))

        # Changing field 'Startup.first_pitch_date'
        db.alter_column('dashboard_startup', 'first_pitch_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Startup.date_added'
        db.alter_column('dashboard_startup', 'date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

        # Changing field 'Startup.first_contact_date'
        db.alter_column('dashboard_startup', 'first_contact_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Person.date_updated'
        db.alter_column('dashboard_person', 'date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))

        # Changing field 'Person.date_added'
        db.alter_column('dashboard_person', 'date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

        # Changing field 'Review.date'
        db.alter_column('dashboard_review', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dashboard.person': {
            'Meta': {'object_name': 'Person'},
            'background': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'reference': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reference_source': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dashboard.ReferenceSource']", 'null': 'True', 'blank': 'True'})
        },
        'dashboard.referencesource': {
            'Meta': {'object_name': 'ReferenceSource'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dashboard.review': {
            'Meta': {'object_name': 'Review'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_step': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'}),
            'reviewer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'startup': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dashboard.Startup']", 'null': 'True'})
        },
        'dashboard.startup': {
            'Meta': {'object_name': 'Startup'},
            'competitors': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_contact_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_pitch_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'milestones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'money': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'next_step': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'}),
            'one_pager': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dashboard.Person']", 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'L'", 'max_length': '1'}),
            'problem': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reference': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reference_source': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dashboard.ReferenceSource']", 'null': 'True', 'blank': 'True'}),
            'slide_deck': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'stage': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'term_sheet': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'users': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['dashboard']
