from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test$',views.doTest,name='doTest'),
    url(r'^$',views.index,name='index'),
]