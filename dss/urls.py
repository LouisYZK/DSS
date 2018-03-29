from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

app_name = 'mainsite'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]