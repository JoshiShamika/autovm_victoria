from django.conf.urls import url

from monitor_dashboard.content.monitor_dashboard_panel import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]