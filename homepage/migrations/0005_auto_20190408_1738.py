# Generated by Django 2.1.7 on 2019-04-08 21:38

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_slide_file_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='file_address',
        ),
        migrations.AddField(
            model_name='slide',
            name='file',
            field=models.FileField(default='', upload_to=homepage.models.get_file_path),
        ),
    ]
