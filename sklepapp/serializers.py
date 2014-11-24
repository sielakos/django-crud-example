from sklepapp.models import Product, Department, Employee
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.RelatedField()

    class Meta:
        model = Product
        fields = ('barcode', 'name', 'price', 'supplier', 'department')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    product_set = serializers.PrimaryKeyRelatedField(many=True)
    employee_set = serializers.PrimaryKeyRelatedField(many=True)
    manager = serializers.RelatedField()

    class Meta:
        model = Department
        fields = ('id', 'name', 'manager', 'product_set', 'employee_set')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.RelatedField()
    class Meta:
        model = Employee
        fields = ('id', 'name', 'surname', 'salary', 'department')