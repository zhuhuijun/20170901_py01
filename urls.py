from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csvt01.views.home', name='home'),
    # url(r'^csvt01/', include('csvt01.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/index/$','blog.views.index'),
    url(r'^calc/index/$','calc.views.index'),
    url(r'^add/$','calc.views.add',name='add'), 
    url(r'^add2/(\d+)/(\d+)/$', 'calc.views.add2', name='add2'),
)
