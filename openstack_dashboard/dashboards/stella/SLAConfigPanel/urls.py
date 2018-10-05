from django.conf.urls import url

from openstack_dashboard.dashboards.stella.SLAConfigPanel import views


urlpatterns = [
    url(r'^$', views.SLAConfigView.as_view(), name='index'),
]
