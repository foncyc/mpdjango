
from django.conf.urls import url
from django.contrib import admin
from beta import views

urlpatterns = [
    url(r'^$', views.show_beta, name='beta_home'),
    url(r'^error', views.show_error, name='beta_error'),
    url(r'^out', views.show_logout, name='beta_out'),
]
