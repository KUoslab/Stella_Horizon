from django.conf.urls import url

from openstack_dashboard.dashboards.mydashboard.SLAConfigPanel import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
