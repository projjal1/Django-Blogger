# Generated by Django 3.0 on 2020-11-30 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='pic_folder/None/no-img.png', upload_to='pic_folder/'),
        ),
    ]
