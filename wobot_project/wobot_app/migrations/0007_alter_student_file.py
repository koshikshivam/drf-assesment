# Generated by Django 4.1 on 2022-08-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wobot_app', '0006_remove_student_rdocs_student_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='file',
            field=models.FileField(upload_to='files'),
        ),
    ]
