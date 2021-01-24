# Generated by Django 3.1.4 on 2021-01-12 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0003_studentcourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentcourse',
            name='courses',
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='courses',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='lms.course'),
            preserve_default=False,
        ),
    ]
