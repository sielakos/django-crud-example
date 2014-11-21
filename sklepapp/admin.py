from django.contrib import admin
from sklepapp.models import Product, Department, Employee

admin.site.register(Employee)

class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline, ProductInline]

admin.site.register(Department, DepartmentAdmin)


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)