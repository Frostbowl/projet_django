# Generated by Django 5.0.6 on 2024-07-06 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0002_alter_media_date_emprunt_alter_media_emprunteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='emprunteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='media_emprunt', to='bibliothecaire.emprunteur'),
        ),
    ]
