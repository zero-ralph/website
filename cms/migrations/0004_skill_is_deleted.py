# Generated by Django 3.1 on 2020-08-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
