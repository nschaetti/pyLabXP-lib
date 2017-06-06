
from django.conf.urls import url, include
from . import views
from rest_framework import routers


# Rest Framework router
router = routers.DefaultRouter()
router.register(r'^exp/(?P<lab>[\w\s]+)/(?P<exp>[\w\s]+)/(?P<instance>\d+)/results', views.ResultViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$', views.home, name="home"),
    url(r'^exp/(?P<lab_name>[\w\s]+)$', views.list_experiences, name="list_experience"),
    url(r'^exp/(?P<lab_name>[\w\s]+)/(?P<exp_name>[\w\s]+)$', views.list_instances, name="list_instances"),
]
