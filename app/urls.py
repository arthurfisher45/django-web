from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.instrument_sum, name='instrument_sum'),
]