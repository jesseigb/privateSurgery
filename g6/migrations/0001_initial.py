# Generated by Django 4.1.1 on 2022-10-12 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateTimeField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('contact_number', models.IntegerField(max_length=15)),
                ('personal_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g6.doctor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=200)),
                ('time', models.DateTimeField(max_length=200)),
                ('issue', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g6.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=200)),
                ('time', models.DateTimeField(max_length=200)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g6.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=200)),
                ('time', models.DateTimeField(max_length=200)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g6.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g6.patient')),
            ],
        ),
    ]
