# Generated by Django 2.1.1 on 2018-10-06 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0002_auto_20181005_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='ProAboutUs',
            new_name='proAboutUs',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='ProArea',
            new_name='proArea',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='ProCreationDate',
            new_name='proCreationDate',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='ProDescription',
            new_name='proDescription',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='ProFrase',
            new_name='proFrase',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='ProName',
            new_name='proName',
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='ProVideo',
            new_name='proVideo',
        ),
        migrations.RenameField(
            model_name='rolinfo',
            old_name='RolLocation',
            new_name='rolLocation',
        ),
        migrations.RenameField(
            model_name='rolinfo',
            old_name='cantidad',
            new_name='rolcantidad',
        ),
    ]
