# Generated by Django 4.2.1 on 2023-11-30 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0005_alter_workshopnumber_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workshopnumber',
            options={'verbose_name_plural': 'Наименование(номер) корпуса'},
        ),
    ]
