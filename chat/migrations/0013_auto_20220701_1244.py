# Generated by Django 3.1.4 on 2022-07-01 07:44

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_all_threads_un_seen_count1'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=chat.models.generate_file_path),
        ),
        migrations.AddField(
            model_name='chat',
            name='voice_note',
            field=models.FileField(blank=True, null=True, upload_to=chat.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='chat',
            name='message_text',
            field=models.TextField(blank=True),
        ),
    ]
