from django.contrib import admin
from equipment.models import Machine, Orders, MachineGroup


class OrdersInline(admin.TabularInline):
    model = Orders
    extra = 1

@admin.register(MachineGroup)
class MachineGroupAdmin(admin.ModelAdmin):
    list_display = [
        "group"
    ]
    list_filter = ["group"]


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    inlines = [OrdersInline]

    list_display = [
        "name",
        "photo",
        "equipment_group",
        "status",
        "factory_floor"
    ]
    list_filter = ["equipment_group", "status"]


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        "equipment_name",
        "short_description",
        "status",
        "orders_files",
        "created_at",
        "updated_at"
    ]
    list_filter = ["status"]
