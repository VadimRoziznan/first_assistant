# Generated by Django 4.2.1 on 2023-11-30 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_workshopnumber_machine_equipment_workshop_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workshopnumber',
            options={'verbose_name_plural': 'Номер цеха'},
        ),
        migrations.AlterModelTable(
            name='workshopnumber',
            table='WorkshopNumber',
        ),
    ]