# Generated by Django 2.1.7 on 2019-04-08 21:40

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20190408_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='file_url',
            field=models.CharField(default=models.FileField(default='', upload_to=homepage.models.get_file_path), max_length=2000),
        ),
    ]
