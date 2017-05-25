from django.conf.urls import patterns, include, url
from django.contrib import admin
from calc import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^(?P<num1>\d+)\+(?P<num2>\d+)', 'calc.views.suma'),
	url(r'^(?P<num1>\d+)\-(?P<num2>\d+)', 'calc.views.resta'),
	url(r'^(?P<num1>\d+)\*(?P<num2>\d+)', 'calc.views.producto'),
	url(r'^(?P<num1>\d+)\/(?P<num2>\d+)', 'calc.views.division'),
)
