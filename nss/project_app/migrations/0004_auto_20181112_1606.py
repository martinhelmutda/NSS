# Generated by Django 2.1.1 on 2018-11-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0003_auto_20181112_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_project',
            name='up_status_text',
        ),
        migrations.AddField(
            model_name='status',
            name='status_text',
            field=models.CharField(default='', max_length=40),
        ),
    ]
