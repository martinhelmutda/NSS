# Generated by Django 2.1.1 on 2018-11-16 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_auto_20181112_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pro_video',
            field=models.URLField(),
        ),
    ]
