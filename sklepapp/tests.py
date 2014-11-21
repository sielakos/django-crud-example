from django.test import TestCase
from sklepapp.models import Product, Department
from django.core.urlresolvers import reverse


class ProductUnicodeTest(TestCase):
    def test_converts_product_unicode(self):
        product = Product(name='cukier', price=4.5, supplier='Biedronka')

        self.assertEqual(unicode(product), product.name)


class DepartmentListViewTest(TestCase):
    def test_department_view(self):
        Department.objects.create(name='ciastka')

        response = self.client.get(reverse('sklepapp:departments'))

        self.assertQuerysetEqual(
            response.context['department_list'],
            ['<Department: ciastka>']
        )

        self.assertContains(response, 'ciastka')