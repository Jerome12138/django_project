# Generated by Django 3.0.3 on 2020-02-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_videodata_ctime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videodata',
            name='id',
        ),
        migrations.AlterField(
            model_name='videodata',
            name='vod_id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, unique=True),
        ),
    ]
