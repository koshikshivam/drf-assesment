# Generated by Django 4.1 on 2022-08-23 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wobot_app', '0003_file_remove_student_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
        migrations.AddField(
            model_name='student',
            name='file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
