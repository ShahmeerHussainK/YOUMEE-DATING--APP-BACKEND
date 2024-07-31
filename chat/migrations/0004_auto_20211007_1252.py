# Generated by Django 3.0.2 on 2021-10-07 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_profile_max_interested_age'),
        ('chat', '0003_auto_20211001_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_receiver', to='core.User_Profile'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to='core.User_Profile'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_user1', to='core.User_Profile'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_user2', to='core.User_Profile'),
        ),
    ]
