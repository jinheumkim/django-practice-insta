# Generated by Django 4.2.7 on 2024-01-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_rename_likecount_feed_like_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
