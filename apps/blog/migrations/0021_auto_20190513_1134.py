# Generated by Django 2.1.7 on 2019-05-13 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20190513_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='unique_id',
            field=models.CharField(default='article_uuid=84ddf400-cdf4-4be1-8a09-a56504d92fb1', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='articlecol',
            name='unique_id',
            field=models.CharField(default='articlecol_uuid=44173529-dac7-4bf8-9e8c-0ba30765fd94', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment', verbose_name='被评论用户'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='unique_id',
            field=models.CharField(default='comment_uuid=f40ef2cd-81e8-4e31-8336-127fd8f31b1a', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='unique_id',
            field=models.CharField(default='reward_uuid=9ae5647f-e3d0-4f3d-98ff-52494ca545a1', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='unique_id',
            field=models.CharField(default='tag_uuid=9c282bd2-5eb4-42b7-ae5b-3597901e88a2', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='type',
            name='unique_id',
            field=models.CharField(default='type_uuid=4cbd8cb0-e2a8-4f8c-91f8-d6d99fef6b79', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
    ]
