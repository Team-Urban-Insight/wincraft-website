# Generated by Django 3.0.7 on 2020-08-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queries',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
