# Generated by Django 4.2.3 on 2023-08-08 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0009_delete_all_appointment_remove_user_appointments_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='customers',
        ),
    ]
