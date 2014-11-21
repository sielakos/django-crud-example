from django.db import models


class Product(models.Model):
    barcode = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    supplier = models.CharField(max_length=250)
    department = models.ForeignKey('Department', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ForeignKey('Employee', related_name='managed_departments', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    salary = models.FloatField()
    department = models.ForeignKey('Department', null=True, blank=True)

    def __unicode__(self):
        return self.name + ' ' + self.surname


