# Generated by Django 4.1.6 on 2023-04-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='static/default.webp', upload_to='static/images'),
        ),
    ]
