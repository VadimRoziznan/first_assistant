# Generated by Django 4.2.1 on 2023-12-01 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0012_orders_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=250, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Причина заявки',
                'db_table': 'Reason',
            },
        ),
        migrations.AddField(
            model_name='orders',
            name='order_reason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders_reason', to='equipment.reason', to_field='reason'),
        ),
    ]