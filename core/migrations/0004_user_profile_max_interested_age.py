# Generated by Django 3.0.4 on 2021-09-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_profile_popup_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='max_interested_age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]