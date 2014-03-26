from django.conf.urls import patterns, url

from assault_app import views

urlpatterns = patterns('',
    url(r'^$', views.all_schools, name='assault_app_all_schools'),
    url(r'^resources/$', views.resources, name='assault_app_resources'),
    url(r'^about/$', views.about, name='assault_app_about'),
    url(r'^(?P<pk>\d+)$', views.school, name='assault_app_school'),
    url(r'^add_comment/$', views.add_comment, name="assault_app_add_comment"),
    url(r'^add_comment.html/$', views.add_comment, name="post_form_add_comment"),
    )