# Generated by Django 4.0.3 on 2022-03-31 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbarberia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turno',
            name='horario',
        ),
    ]