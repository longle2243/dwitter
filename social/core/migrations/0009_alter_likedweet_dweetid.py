# Generated by Django 3.2.11 on 2022-11-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20221104_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likedweet',
            name='dweetid',
            field=models.CharField(max_length=140),
        ),
    ]
