# Generated by Django 4.2.1 on 2023-11-30 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0007_alter_machine_equipment_workshop_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='workshop_number',
        ),
    ]