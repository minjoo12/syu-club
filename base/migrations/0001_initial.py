# Generated by Django 3.1.2 on 2021-08-22 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('club_id', models.AutoField(primary_key=True, serialize=False)),
                ('club_name', models.CharField(blank=True, max_length=200, null=True)),
                ('main_club', models.IntegerField(blank=True, null=True)),
                ('club_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('club_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('club_logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('sns_link', models.CharField(blank=True, max_length=500, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=500, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=500, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=500, null=True)),
                ('form_link', models.CharField(blank=True, max_length=500, null=True)),
                ('recruitment_content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClubTypes',
            fields=[
                ('club_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('club_type_name', models.CharField(blank=True, max_length=200, null=True)),
                ('club_type_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('club_type', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=150)),
                ('post_content', models.CharField(blank=True, max_length=3000, null=True)),
                ('post_img', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.clubs')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.authuser')),
            ],
        ),
        migrations.AddField(
            model_name='clubs',
            name='club_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.clubtypes'),
        ),
        migrations.AddField(
            model_name='clubs',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.authuser'),
        ),
    ]
