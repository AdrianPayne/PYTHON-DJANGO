from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<num>\d+)', 'acorta.views.recurso'),
    url(r'^$', 'acorta.views.main'),
    url(r'^.', 'acorta.views.error'),
]
