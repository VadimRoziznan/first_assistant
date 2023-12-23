# Generated by Django 4.2.1 on 2023-12-23 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0021_orderitems_quantity_orderitems_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_reason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_reason', to='equipment.reason', to_field='reason'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.TextField(choices=[('DRAFT', 'Черновик'), ('OPEN', 'Открыто'), ('FULFILLED', 'Исполнено'), ('NOT_RELEVANT', 'Неактуально')], default='OPEN'),
        ),
    ]
