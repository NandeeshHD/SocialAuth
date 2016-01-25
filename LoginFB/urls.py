from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='account/login.html'), name='Sign In'),
    url(r'^accounts/home/', TemplateView.as_view(template_name='account/home.html'), name='home'),
    url(r'^accounts/', include('allauth.urls')),
)