# Generated by Django 4.1.6 on 2024-04-13 11:27

from django.db import migrations, models
import network.models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_alter_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=network.models.filepath),
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
