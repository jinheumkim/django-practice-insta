# Generated by Django 4.2.7 on 2023-11-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_remove_feed_like_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=254)),
                ('image', models.TextField()),
                ('nickname', models.CharField(max_length=24, unique=True)),
                ('name', models.CharField(max_length=24)),
            ],
        ),
    ]