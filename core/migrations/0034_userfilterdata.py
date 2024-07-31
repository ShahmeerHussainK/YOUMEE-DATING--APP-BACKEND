# Generated by Django 3.1.4 on 2022-12-16 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_user_profile_is_restored'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFilterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('editprofile_gender_checkboxman', 'Male'), ('editprofile_gender_checkboxwoman', 'Female')], max_length=100)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('kids', models.CharField(blank=True, choices=[('partener_kids_yes', 'Yes'), ('partener_kids_no', 'No')], max_length=100)),
                ('drink', models.CharField(blank=True, choices=[('partener_drink_frequently', 'Frequently'), ('partener_drink_socially', 'Socially'), ('partener_drink_never', 'Never')], max_length=100)),
                ('smoke', models.CharField(blank=True, choices=[('partener_drink_frequently', 'Frequently'), ('partener_drink_socially', 'Socially'), ('partener_drink_never', 'Never')], max_length=100)),
                ('religion', models.CharField(blank=True, choices=[('Christian', 'Christian'), ('Buddhist', 'Buddhist'), ('Catholic', 'Catholic'), ('Islam', 'Islam'), ('Atheist', 'Atheist'), ('hindui', 'Spirituality')], max_length=20)),
                ('exercise', models.CharField(blank=True, choices=[('partener_exercise_active', 'Active'), ('partener_exercise_sometime', 'Sometimes'), ('partener_exercise_almostNever', 'Almost Never')], max_length=200)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('education', models.CharField(blank=True, choices=[('update_education_college_checkbox', 'College'), ('update_education_highschool_checkbox', 'High School'), ('update_education_BAC_checkbox', 'BAC Level'), ('update_university_checkbox', 'University Diploma')], max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_filter_data', to='core.user_profile')),
            ],
        ),
    ]
