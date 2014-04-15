from django.conf.urls import patterns, include, url

from django.contrib import admin

from MyFreq import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyFreq.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.UploadView.as_view(), name = "upload_file"),
    url(r'^result$', views.ResultView.as_view(), name = "result"),
)
