# Generated by Django 2.1.1 on 2018-10-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_auto_20181030_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Ubicación'),
        ),
    ]
