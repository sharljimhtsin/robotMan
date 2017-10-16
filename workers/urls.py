from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test$', views.doTest, name='doTest'),
    url(r'^trigger$', views.start_fork_again, name='start_fork_again'),
    url(r'^triggerOmit$', views.start_fork, name='start_fork'),
    url(r'^triggerOld$', views.start, name='start'),
    url(r'^excel$', views.parseExcel, name='parseExcel'),
    url(r'^$', views.index, name='index'),
]
