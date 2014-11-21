from django.shortcuts import render, redirect
from sklepapp.models import Product, Department, Employee
from django.views import generic
from rest_framework import viewsets
from sklepapp.serializers import ProductSerializer, DepartmentSerializer, EmployeeSerializer


def index(request):
    return redirect('sklepapp:departments')


class DepartmentListView(generic.ListView):
    model = Department


class DepartmentView(generic.DetailView):
    model = Department


class ProductListView(generic.ListView):
    model = Product


class EmployeeListView(generic.ListView):
    model = Employee


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer