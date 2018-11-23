# Generated by Django 2.1.1 on 2018-11-23 04:36

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('category', models.CharField(default='', max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('city', models.CharField(default='', max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(default='', max_length=40)),
                ('pro_description', ckeditor.fields.RichTextField(max_length=5000, verbose_name='Descripción')),
                ('pro_video', embed_video.fields.EmbedVideoField()),
                ('order', models.SmallIntegerField(default=0, verbose_name='Orden')),
                ('pro_about_us', models.TextField(default='', max_length=800)),
                ('pro_phrase', models.CharField(default='', max_length=200)),
                ('pro_creation_date', models.DateField()),
                ('pro_img', models.ImageField(blank=True, default='', upload_to='pro_img')),
                ('pro_group', models.BooleanField()),
                ('pro_save_times', models.PositiveIntegerField(default=0)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('pro_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='project_app.category')),
                ('pro_city', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='project_app.city')),
            ],
            options={
                'verbose_name': 'project_app',
                'verbose_name_plural': 'project_app',
                'ordering': ['order', 'pro_name'],
            },
        ),
        migrations.CreateModel(
            name='project_rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='project', to='project_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='projectImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_img', models.ImageField(blank=True, default='', upload_to='pro_img')),
                ('pro', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='rolInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_name', models.CharField(default='', max_length=150)),
                ('rol_name_other', models.CharField(blank=True, default='', max_length=150)),
                ('rol_due_date', models.DateField()),
                ('rol_amount', models.PositiveIntegerField(default=1)),
                ('rol_description', models.TextField(default='', max_length=800)),
                ('rol_city', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='project_app.city')),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('state', models.CharField(default='', max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('status', models.CharField(default='', max_length=50, primary_key=True, serialize=False, unique=True)),
                ('status_text', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('subcategory', models.CharField(default='', max_length=50, primary_key=True, serialize=False, unique=True)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='project_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='user_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_project', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='up_project', to='project_app.project')),
                ('up_rolInfo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='up_rolInfo', to='project_app.rolInfo')),
                ('up_status', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='upstatus', to='project_app.status')),
                ('up_user', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='rolinfo',
            name='rol_state',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='project_app.state'),
        ),
        migrations.AddField(
            model_name='project_rol',
            name='rol',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='rolInfo', to='project_app.rolInfo'),
        ),
        migrations.AddField(
            model_name='project',
            name='pro_roles',
            field=models.ManyToManyField(through='project_app.project_rol', to='project_app.rolInfo'),
        ),
        migrations.AddField(
            model_name='project',
            name='pro_state',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='project_app.state'),
        ),
        migrations.AddField(
            model_name='project',
            name='pro_subcategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='project_app.subcategory'),
        ),
        migrations.AddField(
            model_name='project',
            name='pro_user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='project_app.state'),
        ),
    ]
