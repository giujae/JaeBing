# Generated by Django 3.1.3 on 2023-05-18 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_no', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=100)),
                ('release_date', models.DateField(null=True)),
                ('poster_path', models.CharField(max_length=200)),
                ('backdrop_path', models.CharField(max_length=255, null=True)),
                ('adult', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('original_language', models.CharField(max_length=50)),
                ('overview', models.TextField()),
                ('vote_count', models.IntegerField(default=0)),
                ('vote_average', models.FloatField(default=0.0)),
                ('popularity', models.FloatField(default=0.0)),
                ('admin_reg', models.BooleanField(default=False)),
                ('genre_ids', models.ManyToManyField(related_name='movie_genres', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rate', models.IntegerField(default=0)),
                ('like', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
