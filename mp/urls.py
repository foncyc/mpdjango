from django.conf.urls import url, include
from django.contrib import admin
from beta import views

urlpatterns = [
    url(r'^$', views.show_beta),
    url(r'^admin/', admin.site.urls),
    url(r'^beta/', include('beta.urls')),
    url(r'^accounts/', include('accounts.urls')),
]
