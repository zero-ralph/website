# Generated by Django 3.1 on 2020-08-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_skill_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='services_sub_header',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
