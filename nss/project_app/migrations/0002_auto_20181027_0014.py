# Generated by Django 2.1.1 on 2018-10-27 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolinfo',
            name='rol_name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
