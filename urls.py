from django.conf.urls import patterns, include, url

from django.contrib import admin

from MyFreq import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyFreq.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name = "index"),
    url(r'^upload$', views.UploadView.as_view(), name = "upload_file"),
)
