# Generated by Django 3.1.4 on 2022-07-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_user_profile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='like_and_dislike',
            name='match_seen',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]