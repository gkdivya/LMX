# Generated by Django 3.1.4 on 2021-01-18 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0011_auto_20210118_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentassignment',
            name='student_course',
        ),
        migrations.AddField(
            model_name='studentassignment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='studentassignments', to='auth.user'),
            preserve_default=False,
        ),
    ]
