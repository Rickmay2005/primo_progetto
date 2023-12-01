# Generated by Django 4.2.5 on 2023-12-01 09:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articolo_options_alter_giornalista_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='articolo',
            name='data',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='articolo',
            name='visualizzazioni',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='giornalista',
            name='anno_di_nascita',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
