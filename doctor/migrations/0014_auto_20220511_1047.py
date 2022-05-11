# Generated by Django 3.2.6 on 2022-05-11 10:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0013_alter_doctor_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='avatar',
            field=models.ImageField(default='doctors/default.png', upload_to='doctors/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
    ]
