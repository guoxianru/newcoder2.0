# Generated by Django 2.1.7 on 2019-05-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20190513_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemsg',
            name='unique_id',
            field=models.CharField(default='leavemsg_uuid=42ce696c-bc34-4053-bfa6-ad8125cd18f1', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default='user_uuid=6fd19b77-1956-4f85-865e-a0fb94445a12', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
    ]