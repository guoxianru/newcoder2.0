# Generated by Django 2.1.7 on 2019-05-12 20:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190512_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemsg',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('fa5f6656-aea6-4801-8bc0-4fde3ccf0c19'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('0f98ca83-14f6-4078-addf-3d4a532612d7'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
    ]
