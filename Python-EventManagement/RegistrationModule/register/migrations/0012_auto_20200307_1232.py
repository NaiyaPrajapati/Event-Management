# Generated by Django 3.0.2 on 2020-03-07 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_customerevent_event_managerevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_video_filelocation',
            field=models.ImageField(upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='previous_event_image_filelocation',
            field=models.ImageField(upload_to='images/'),
        ),
    ]