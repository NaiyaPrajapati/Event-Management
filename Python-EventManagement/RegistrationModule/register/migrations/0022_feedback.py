# Generated by Django 3.0.2 on 2020-03-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0021_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_ID', models.CharField(max_length=20)),
                ('feedback', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]