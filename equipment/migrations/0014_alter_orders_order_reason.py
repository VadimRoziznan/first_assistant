# Generated by Django 4.2.1 on 2023-12-01 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0013_reason_orders_order_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_reason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders_reason', to='equipment.reason', to_field='reason'),
        ),
    ]
