# Generated by Django 2.1.1 on 2018-10-04 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rolinfo',
            name='RolArea',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='appOne.area'),
        ),
    ]
