# Generated by Django 5.1.1 on 2024-10-10 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0013_aboutsitemodel_description_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='question_title')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='TeamAboutModul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='team_about_module_title')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='team_about_module_images', verbose_name='team_about_module_image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Team About Module',
                'verbose_name_plural': 'Team About Modules',
            },
        ),
    ]
