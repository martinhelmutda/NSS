# Generated by Django 2.1.1 on 2018-10-12 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectoimagen',
            name='proyecto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appOne.proyecto'),
        ),
    ]