# Generated by Django 5.0.4 on 2024-05-04 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='ocupation',
            new_name='ocuPatIon',
        ),
    ]