# Generated by Django 4.2.3 on 2023-08-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0005_all_appointment_user_appointments_delete_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_appointments',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user_appointments',
            name='service',
            field=models.CharField(max_length=100),
        ),
    ]
