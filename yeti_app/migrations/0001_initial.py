# Generated by Django 3.1.5 on 2021-01-05 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blueprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blueprint', models.ImageField(upload_to='team_blueprints')),
                ('info', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, unique=True)),
                ('users_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='team_images')),
                ('comment', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('login', models.CharField(max_length=63, unique=True)),
                ('password', models.CharField(max_length=127)),
                ('mail', models.CharField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=127)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('photo', models.ImageField(upload_to='user_photos')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=25)),
                ('video_path', models.CharField(max_length=255)),
                ('info', models.CharField(max_length=255)),
                ('place', models.IntegerField()),
                ('blueprint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yeti_app.blueprint')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yeti_app.image')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('role', models.CharField(max_length=20)),
                ('team_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yeti_app.team')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yeti_app.user')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yeti_app.competition')),
            ],
        ),
    ]
