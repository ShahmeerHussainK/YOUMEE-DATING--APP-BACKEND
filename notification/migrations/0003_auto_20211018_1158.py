# Generated by Django 3.0.2 on 2021-10-18 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_user_profile_power_like_count'),
        ('notification', '0002_auto_20211018_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationRoomRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_room_name', models.CharField(max_length=100, null=True)),
                ('is_enabled', models.BooleanField(blank=True, default=False, null=True)),
                ('is_deleed', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_room_user1', to='core.User_Profile')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_room_user2', to='core.User_Profile')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='NotificationRoom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='NotificationRoom', to='notification.NotificationRoomRoom'),
        ),
    ]
