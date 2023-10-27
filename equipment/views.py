import os

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import F

from pathlib import Path
from equipment.models import Orders, Machine
from equipment.serializers import OrdersSerializer, MachineNameSerializer

BASE_DIR = Path(__file__).resolve().parent.parent

class OrdersViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


class MachineViewSet(ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineNameSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


def home_view(request):
    print(os.path.join(BASE_DIR, 'static'))
    template = "equipment/home.html"
    context = {}
    return render(request, template, context)


def orders_view(request):
    template = "equipment/orders.html"

    order_status = request.GET.get('order_status', 'ALL')
    equipment_group = request.GET.get('equipment_class', 'ALL')
    query = request.GET.get('query')
    if query:
        dataset = Orders.objects.raw(
        '''
            SELECT * FROM "Orders"
            JOIN "Machine" ON "Orders".equipment_name_id = "Machine".id
            WHERE
            "Orders".status LIKE %s
            OR
            "Machine"."name" LIKE %s
            OR
            "Orders".short_description LIKE %s
            ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
    else:
        dataset = Orders.objects.raw(
        '''
            SELECT * FROM "Orders"
            JOIN "Machine" ON "Orders".equipment_name_id = "Machine".id
            WHERE (CASE
                    WHEN %s != 'ALL' THEN "Machine"."group" = %s
                    ELSE "Machine"."group" IS NOT NULL
                END)
            AND (CASE
                    WHEN %s != 'ALL' THEN "Orders".status = %s
                    ELSE "Orders".status IS NOT NULL
                END);
        ''', (equipment_group, equipment_group, order_status, order_status))

    # dataset = Orders.objects.select_related('equipment_name').filter(
    #     (Q(equipment_name__group=equipment_group) | Q(
    #         equipment_name__group__isnull=True)) if equipment_group != 'ALL' else Q(
    #         equipment_name__group__isnull=False),
    #     (Q(status=order_status) | Q(status__isnull=True)) if order_status != 'ALL' else Q(status__isnull=False)
    # )

    context = {
        "orders_and_equipment": dataset
    }
    return render(request, template, context)

def create_order (request):
    template = "equipment/create_order.html"
    machine = Machine.objects.raw(
        '''
            SELECT * FROM "Machine"
            ''')
    context = {
        "equipment_class": machine
    }
    return render(request, template, context)

def equipment_view(request):
    context = {}
    return render(request, "equipment/home.html", context)

