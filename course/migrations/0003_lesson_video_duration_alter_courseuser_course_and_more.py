# Generated by Django 5.0.2 on 2024-02-14 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_rating_alter_feedback_stars_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video_duration',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='courseuser',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_users', to='course.course'),
        ),
        migrations.AlterField(
            model_name='lessonuser',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_users', to='course.lesson'),
        ),
    ]