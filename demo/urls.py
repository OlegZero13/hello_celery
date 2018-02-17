from django.conf.urls import url

from . import views

app_name = 'demo'

urlpatterns= [
    url(r'^index/$', views.index, name="index"),
    url(r'^test_page/$', views.test_page, name="test_page"),
    url(r'^start_test/$', views.start_test, name="start_test"),
    url(r'^[\s\S]*/update_status/$', views.update_status, name='update_status'),
    url(r'^abort_test/$', views.abort_test, name="abort_test"),

    url(r'^dynamic/$', views.dynamic, name="dynamic"),
]

