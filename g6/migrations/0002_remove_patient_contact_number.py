# Generated by Django 4.1.1 on 2022-10-12 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('g6', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='contact_number',
        ),
    ]
