from django.db import models


class OrdersStatusChoices(models.TextChoices):
    """Статусы заявок."""

    OPEN = "OPEN", "Открыто"
    FULFILLED = "FULFILLED", "Исполнено"
    NOT_RELEVANT = "NOT_RELEVANT", "Неактуально"
    DRAFT = "DRAFT", "Черновик"


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


class Machine(models.Model):

    def machine_file_path(self, filename):
        # Получаем имя связанного оборудования
        name = self.name

        # Формируем путь: "photos/machines/<equipment_name>/<filename>"
        path = f'machines/{name}/photo/{filename}'

        return path

    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to=machine_file_path,
        null=True,
        blank=True
    )

    status = models.TextField(
        choices=MachineStatusChoices.choices,
        default=MachineStatusChoices.OPERATED,
    )
    group = models.TextField(
        choices=MachineGroupChoices.choices,
        default=MachineGroupChoices.OTHER,
    )
    factory_floor = models.IntegerField(default=1)

    class Meta:
        db_table = 'Machine'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return self.name


class Archive(models.Model):
    name = models.CharField(max_length=100)


class Orders(models.Model):

    def orders_file_path(instance, filename):
        # Получаем имя связанного оборудования
        equipment_name = instance.equipment_name.name

        # Формируем путь: "photos/machines/<equipment_name>/<filename>"
        path = f'orders/{equipment_name}/{filename}'

        return path


    equipment_name = models.ForeignKey(
        Machine, on_delete=models.CASCADE,
        related_name="machine"
    )
    short_description = models.TextField(
        max_length=500,
        null=True
    )
    status = models.TextField(
        choices=OrdersStatusChoices.choices,
        default=OrdersStatusChoices.OPEN,
    )
    orders_files = models.FileField(upload_to=orders_file_path, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Orders'
        verbose_name_plural = 'Заявки'


class Stock(models.Model):
    pass
