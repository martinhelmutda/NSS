# Generated by Django 2.1.1 on 2018-10-25 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pro_category',
        ),
        migrations.RemoveField(
            model_name='project',
            name='pro_location',
        ),
        migrations.RemoveField(
            model_name='project',
            name='pro_roles',
        ),
        migrations.RemoveField(
            model_name='projectimg',
            name='pro',
        ),
        migrations.RemoveField(
            model_name='rolinfo',
            name='rol_location',
        ),
        migrations.RemoveField(
            model_name='rolinfo',
            name='rol_name',
        ),
        migrations.DeleteModel(
            name='category',
        ),
        migrations.DeleteModel(
            name='location',
        ),
        migrations.DeleteModel(
            name='project',
        ),
        migrations.DeleteModel(
            name='projectImg',
        ),
        migrations.DeleteModel(
            name='rol',
        ),
        migrations.DeleteModel(
            name='rolInfo',
        ),
    ]