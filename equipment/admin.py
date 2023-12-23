from django.contrib import admin
from equipment.models import Machine, Orders, MachineGroup, WorkshopNumber, SpanNumber, Reason



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
        "machine_status",
        "equipment_workshop_number",
        "equipment_span_number"
    ]
    list_filter = ["equipment_group", "machine_status"]



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        "equipment_name",
        "short_description",
        "status",
        "order_file_path",
        "created_at",
        "updated_at",
        "order_reason"
    ]
    list_filter = ["status"]



@admin.register(WorkshopNumber)
class WorkshopNumberAdmin(admin.ModelAdmin):
    list_display = [
        "workshop_number"
    ]
    list_filter = ["workshop_number"]


@admin.register(SpanNumber)
class SpanNumberAdmin(admin.ModelAdmin):
    list_display = [
        "span_number"
    ]
    list_filter = ["span_number"]


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = [
        "reason"
    ]
    list_filter = ["reason"]