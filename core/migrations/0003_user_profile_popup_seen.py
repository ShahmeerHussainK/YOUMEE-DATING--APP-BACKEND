# Generated by Django 3.0.4 on 2021-09-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='popup_seen',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
