from django.conf.urls import url
from home.views import index
from home.views import results1
from home.views import results2
from home.views import results3
from home.views import us
from home.views import orders
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<pk>1)/$', results1),
    url(r'^(?P<pk>2)/$', results2),
    url(r'^(?P<pk>3)/$', results3),
    url(r'^(?P<pk>us)/$', us),
    url(r'^(?P<pk>orders)/$', orders),


]




