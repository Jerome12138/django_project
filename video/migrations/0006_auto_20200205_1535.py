# Generated by Django 2.1.4 on 2020-02-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20200205_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlist',
            name='vod_addtime',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requestlist',
            name='vod_continu',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
