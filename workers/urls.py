from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test$', views.doTest, name='doTest'),
    url(r'^trigger$', views.start, name='start'),
    url(r'^excel$', views.parseExcel, name='parseExcel'),
    url(r'^$', views.index, name='index'),
]
