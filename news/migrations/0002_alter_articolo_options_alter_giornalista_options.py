# Generated by Django 4.2.5 on 2023-11-24 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articolo',
            options={'verbose_name': 'Articolo', 'verbose_name_plural': 'Articoli'},
        ),
        migrations.AlterModelOptions(
            name='giornalista',
            options={'verbose_name': 'Giornalista', 'verbose_name_plural': 'Giornalisti'},
        ),
    ]
