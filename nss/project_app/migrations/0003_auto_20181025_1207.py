# Generated by Django 2.1.1 on 2018-10-25 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_projectimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimg',
            name='pro',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project_app.project'),
        ),
    ]