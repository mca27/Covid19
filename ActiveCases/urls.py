from django.conf.urls import url
from . import views

app_name = 'ActiveCases'

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<case_id>[0-9]+)/$', views.details, name='detail'),
]
