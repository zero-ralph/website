# Generated by Django 3.1 on 2020-08-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_about_embed_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='embed_map',
            field=models.TextField(blank=True, null=True),
        ),
    ]
