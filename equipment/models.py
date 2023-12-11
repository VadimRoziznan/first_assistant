import re
from urllib.parse import quote
from django.db import models


class OrdersStatusChoices(models.TextChoices):
    """Статусы заявок."""

    DRAFT = "DRAFT", "Черновик"
    OPEN = "OPEN", "Открыто"
    FULFILLED = "FULFILLED", "Исполнено"
    NOT_RELEVANT = "NOT_RELEVANT", "Неактуально"


class MachineStatusChoices(models.TextChoices):
    """Статусы оборудования."""

    OPERATED = "OPERATED", "Эксплуатируется"
    UNDER_REPAIR = "UNDER_REPAIR", "В ремонте"
    DECOMMISSIONED = "DECOMMISSIONED", "Списано"


class MachineGroupChoices(models.TextChoices):
    """Группы оборудования"""

    HORIZONTAL_BORING_MACHINE = "HORIZONTAL_BORING_MACHINE", "Горизонтально - расточные станки"
    SCREW_CUTTING_MACHINE = "SCREW_CUTTING_MACHINE", "Токарно - винторезные станки"
    TURNING_LATHES_MACHINE = "TURNING_LATHES_MACHINE", "Токарно - карусельные станки"
    FORGING_STAMPING_EQUIPMENT = "FORGING_STAMPING_EQUIPMENT", "Кузнечно - штамповочное оборудование"
    HANDLING_EQUIPMENT = "HANDLING_EQUIPMENT", "Подъемно - транспортное оборудование"
    OTHER = "OTHER", "ДРУГОЕ"


class MachineGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.TextField(
        choices=MachineGroupChoices.choices,
        unique=True
    )

    class Meta:
        db_table = 'MachineGroup'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.group


class WorkshopNumber(models.Model):

    workshop_number = models.CharField(
        max_length=50, null=True, unique=True
    )

    class Meta:
        db_table = 'WorkshopNumber'
        verbose_name_plural = 'Наименование(номер) корпуса'

    def __str__(self):
        return self.workshop_number


class SpanNumber(models.Model):

    span_number = models.IntegerField(unique=True, null=True)

    class Meta:
        db_table = 'SpanNumber'
        verbose_name_plural = 'Номер пролёта'


class Machine(models.Model):

    def machine_file_path(self, filename):
        # Получаем имя связанного оборудования
        name = self.name

        # Формируем путь: "photos/machines/<equipment_name>/<filename>"
        path = f'machines/{name}/photo/{filename}'

        return path

    name = models.CharField(max_length=90)
    photo = models.ImageField(
        upload_to=machine_file_path,
        null=True,
        blank=True
    )
    machine_status = models.TextField(
        choices=MachineStatusChoices.choices,
        default=MachineStatusChoices.OPERATED,
    )
    equipment_group = models.ForeignKey(
        MachineGroup, on_delete=models.PROTECT,
        blank=True,
        related_name="machine_group",
        null=True,
    )
    equipment_workshop_number = models.ForeignKey(
        WorkshopNumber, on_delete=models.PROTECT,
        related_name="machine_workshop_number", null=True, to_field="workshop_number"
    )
    equipment_span_number = models.ForeignKey(
        SpanNumber, on_delete=models.PROTECT,
        related_name="machine_span_number", null=True, to_field="span_number"
    )

    class Meta:
        db_table = 'Machine'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return self.name


class Archive(models.Model):

    name = models.CharField(max_length=100)


class Reason(models.Model):

    reason = models.CharField(
        max_length=250, null=True, unique=True
    )

    class Meta:
        db_table = 'Reason'
        verbose_name_plural = 'Причина заявки'

    def __str__(self):
        return self.reason


class Orders(models.Model):

    def orders_file_path(instance, filename):
        # Получаем имя связанного оборудования
        equipment_name = instance.equipment_name.name
        # Формируем путь: "photos/machines/<equipment_name>/<filename>"
        path = f"orders/{equipment_name}/{filename}"
        return path

    equipment_name = models.ForeignKey(
        Machine, on_delete=models.CASCADE,
        related_name="machine"
    )
    short_description = models.TextField(
        max_length=500,
        null=True,
        default="test"
    )
    status = models.TextField(
        choices=OrdersStatusChoices.choices,
        default=OrdersStatusChoices.OPEN,
    )
    file_name = models.CharField(max_length=90, null=True, blank=True)
    order_file_path = models.FileField(upload_to=orders_file_path, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_reason = models.ForeignKey(
        Reason, on_delete=models.PROTECT,
        related_name="orders_reason", null=True, to_field="reason"
    )
    # reason = models.CharField(max_length=250, null=True, blank=True)



    class Meta:
        db_table = 'Orders'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.status


class OrderItems(models.Model):
    item = models.TextField(max_length=1000, null=True)
    quantity = models.IntegerField(null=True, default=0)
    unit = models.CharField(max_length=10, null=True)
    order = models.ForeignKey(
        Orders, on_delete=models.CASCADE,
        related_name='order', null=True
    )

    class Meta:
        db_table = 'OrderItems'
        verbose_name_plural = 'Пункты'

    def __str__(self):
        return self.item


class Stock(models.Model):
    pass


