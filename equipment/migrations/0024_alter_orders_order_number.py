# Generated by Django 4.2.1 on 2023-12-25 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0023_orders_order_number_alter_orders_order_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_number',
            field=models.IntegerField(verbose_name='Номер заявки в текущем году.'),
        ),
    ]
