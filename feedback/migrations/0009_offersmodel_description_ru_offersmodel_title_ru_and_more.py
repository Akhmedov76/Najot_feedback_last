# Generated by Django 5.1.1 on 2024-10-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0008_alter_problemsmodel_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offersmodel',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='offersmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='offers_title'),
        ),
        migrations.AddField(
            model_name='problemsmodel',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='problemsmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='problems_title'),
        ),
    ]
