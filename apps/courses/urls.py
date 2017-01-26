from django.conf.urls import url, include
from .import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process', views.process),
    url(r'^delete/(?P<course_id>\d+)', views.delete),
    # url(r'^delete', views.delete),
    # url(r'^users$', views.show)
]
