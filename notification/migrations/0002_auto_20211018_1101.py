# Generated by Django 3.0.2 on 2021-10-18 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_user_profile_power_like_count'),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='recever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recever_messages', to='core.User_Profile'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_messages', to='core.User_Profile'),
        ),
    ]