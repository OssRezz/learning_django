# Generated by Django 5.0.7 on 2024-08-07 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_first_app.author'),
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
