# Generated by Django 3.2.6 on 2022-03-14 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duration',
            name='doctor',
        ),
    ]
