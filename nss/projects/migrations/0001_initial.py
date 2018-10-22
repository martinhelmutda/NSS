# Generated by Django 2.1.1 on 2018-10-21 22:22

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('category', models.CharField(default='', max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('location', models.CharField(default='', max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(default='', max_length=40)),
                ('pro_description', models.TextField(default='', max_length=800)),
                ('pro_video', embed_video.fields.EmbedVideoField()),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('pro_about_us', models.TextField(default='', max_length=800)),
                ('pro_phrase', models.CharField(default='', max_length=200)),
                ('pro_creation_date', models.DateField()),
                ('pro_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='projects.category')),
                ('pro_location', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='projects.location')),
            ],
            options={
                'verbose_name': 'projects',
                'verbose_name_plural': 'projects',
                'ordering': ['pro_name'],
            },
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('rol', models.CharField(default='', max_length=15, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='rolInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_due_date', models.DateField()),
                ('rol_amount', models.PositiveIntegerField(default=1)),
                ('rol_description', models.TextField(default='', max_length=800)),
                ('rol_location', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='projects.location')),
                ('rol_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rol')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='pro_roles',
            field=models.ManyToManyField(to='projects.rolInfo'),
        ),
    ]
