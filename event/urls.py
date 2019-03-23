from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.hm, name='hm'),
    url(r'^add/$', views.add, name='add'),
    url(r'^upgrade/$', views.upgrade, name='upgrade')
]