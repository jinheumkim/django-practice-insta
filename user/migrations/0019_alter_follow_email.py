# Generated by Django 4.2.7 on 2023-11-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_remove_follow_user_follow_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]