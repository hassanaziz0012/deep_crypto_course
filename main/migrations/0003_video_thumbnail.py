# Generated by Django 4.0.4 on 2022-11-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_video_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='thumbnails'),
            preserve_default=False,
        ),
    ]
