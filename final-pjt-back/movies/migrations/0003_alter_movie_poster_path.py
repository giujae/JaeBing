# Generated by Django 3.2.18 on 2023-05-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20230522_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
