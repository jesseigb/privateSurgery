# Generated by Django 4.1.1 on 2022-10-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g6', '0002_remove_patient_contact_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reports',
            new_name='Report',
        ),
        migrations.AddField(
            model_name='doctor_availability',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor_availability',
            name='time',
            field=models.TimeField(max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(max_length=200),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200),
        ),
    ]
