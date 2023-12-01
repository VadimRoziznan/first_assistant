import os
from pprint import pprint

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django.db.models import F

from pathlib import Path

from equipment.forms import UploadFileForm
from equipment.models import Orders, Machine, MachineGroup, WorkshopNumber, SpanNumber, Reason
from equipment.serializers import OrdersSerializer, MachineNameSerializer

from datetime import datetime

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
    equipment_group = request.GET.get('equipment_group', 'ALL')
    print(equipment_group)
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
                SELECT * 
                FROM "Orders" 
                INNER JOIN "Machine" ON ("Orders"."equipment_name_id" = "Machine"."id") 
                LEFT OUTER JOIN "MachineGroup" ON ("Machine"."equipment_group_id" = "MachineGroup"."id")
                WHERE (CASE
                    WHEN %s != 'ALL' THEN "MachineGroup"."group" = %s
                    ELSE "Machine"."equipment_group_id" IS NOT NULL
                END)
                AND (CASE
                     WHEN %s != 'ALL' THEN "Orders".status = %s
                     ELSE "Orders".status IS NOT NULL
                END);
	        ''', (equipment_group, equipment_group, order_status, order_status))
    context = {
        "orders_and_equipment": dataset
    }
    return render(request, template, context)


def handle_uploaded_file(f, path):
    with open(path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def create_order (request):
    template = "equipment/create_order.html"
    form = UploadFileForm()
    machines = Machine.objects.raw(
        '''
        SELECT * FROM "Machine";
        ''')
    groups = MachineGroup.objects.raw(
        '''
        SELECT * from "MachineGroup";
        ''')
    workshop_number = WorkshopNumber.objects.all()
    equipment_span_number = SpanNumber.objects.all()
    reason = Reason.objects.all()
    if request.method == "POST":
        equipment_name = 1
        short_description = 'rrrr'
        status = request.POST.get('status')
        order_file = request.FILES["file"]
        date_now = datetime.now().strftime("%d.%m.%Y")
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_order = Orders(
                equipment_name=Machine.objects.get(id=equipment_name)
            )
            new_order.save()
            order = Orders.objects.get(id=new_order.id)
            _, file_extension = os.path.splitext(order_file.name)
            order.file_name = f"Заявка №{new_order.id} от {date_now}{file_extension}"
            order_file.name = f"Заявка '№{new_order.id} от {date_now}{file_extension}"
            order.order_file_path = order_file
            order.save()
    context = {
        "machines": machines,
        "groups": groups,
        "workshop_number": workshop_number,
        "equipment_span_number": equipment_span_number,
        "reason": reason,
        "form": form
    }
    return render(request, template, context)


def equipment_view(request):
    context = {}
    return render(request, "equipment/home.html", context)

