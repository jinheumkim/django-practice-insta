# Generated by Django 4.2.7 on 2023-12-15 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_feed_likecount_feed_nickname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='likecount',
            new_name='like_count',
        ),
    ]