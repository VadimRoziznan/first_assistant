from django.contrib import admin
from equipment.models import Machine, Orders


class OrdersInline(admin.TabularInline):
    model = Orders
    extra = 1


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    inlines = [OrdersInline]
    list_display = [
        "name",
        "photo",
        "group",
        "status",
        "factory_floor"
    ]
    list_filter = ["group", "status"]


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
