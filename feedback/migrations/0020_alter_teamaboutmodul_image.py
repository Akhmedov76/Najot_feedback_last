# Generated by Django 5.1.1 on 2024-10-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0019_appealsmodule_description_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamaboutmodul',
            name='image',
            field=models.ImageField(upload_to='team_avatars/'),
        ),
    ]
