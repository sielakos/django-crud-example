from django.conf.urls import patterns, url, include
from sklepapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^departments$', views.DepartmentListView.as_view(), name='departments'),
    url(r'^department/(?P<pk>\d+)$', views.DepartmentView.as_view(), name='department'),
    url(r'^products$', views.ProductListView.as_view(), name='products'),
    url(r'^employees', views.EmployeeListView.as_view(), name='employees'),
    url(r'^rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)