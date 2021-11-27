# Generated by Django 3.2.8 on 2021-11-27 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='first_name',
            new_name='actor_name',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='last_name',
            new_name='actress_name',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='age',
            new_name='year',
        ),
        migrations.AddField(
            model_name='data',
            name='director_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='movie_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
