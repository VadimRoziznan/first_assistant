from rest_framework import serializers

from equipment.models import Orders, Machine


class MachineNameSerializer(serializers.ModelSerializer):
    """Serializer для оборудования."""

    class Meta:
        model = Machine
        field = (
            "name",
        )


class OrdersSerializer(serializers.ModelSerializer):
    """Serializer для заявок."""
    machine_name = MachineNameSerializer(read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"
