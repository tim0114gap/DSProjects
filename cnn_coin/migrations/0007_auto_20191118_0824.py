# Generated by Django 2.2.1 on 2019-11-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnn_coin', '0006_auto_20191118_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(null=True, upload_to='cnn_coin'),
        ),
    ]
