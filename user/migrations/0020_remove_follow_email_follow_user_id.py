# Generated by Django 4.2.7 on 2023-11-30 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_alter_follow_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='email',
        ),
        migrations.AddField(
            model_name='follow',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
