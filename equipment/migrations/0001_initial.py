# Generated by Django 4.2.1 on 2023-07-08 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/machines/')),
                ('status', models.TextField(choices=[('OPERATED', 'Эксплуатируется'), ('UNDER_REPAIR', 'В ремонте'), ('DECOMMISSIONED', 'Списано')], default='OPERATED')),
                ('group', models.TextField(choices=[('HORIZONTAL_BORING_MACHINE', 'Горизонтально - расточной станок'), ('OTHER', 'ДРУГОЕ')], default='OTHER')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.TextField(max_length=500, null=True)),
                ('status', models.TextField(choices=[('OPEN', 'Открыто'), ('FULFILLED', 'Исполнено'), ('NOT_RELEVANT', 'Неактуально'), ('DRAFT', 'Черновик')], default='OPEN')),
                ('orders_files', models.FileField(null=True, upload_to='orders/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('equipment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machine', to='equipment.machine')),
            ],
        ),
    ]
