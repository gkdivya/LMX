# Generated by Django 3.1.4 on 2021-01-16 16:21

import assignments.models.assignment_model
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_auto_20210116_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='image',
            field=models.ImageField(upload_to=assignments.models.assignment_model.upload_path),
        ),
    ]
