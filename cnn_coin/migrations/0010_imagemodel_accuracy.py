# Generated by Django 2.2.1 on 2019-11-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnn_coin', '0009_auto_20191119_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='accuracy',
            field=models.CharField(default='0', max_length=7),
        ),
    ]
