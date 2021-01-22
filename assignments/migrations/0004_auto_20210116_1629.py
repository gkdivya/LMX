# Generated by Django 3.1.4 on 2021-01-16 10:59

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0003_assignment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(upload_to='uploads/collaborators/%Y/%m/%d'),
        ),
    ]