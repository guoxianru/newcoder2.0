# Generated by Django 2.1.7 on 2019-04-28 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190426_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Type', verbose_name='标签分类'),
            preserve_default=False,
        ),
    ]
