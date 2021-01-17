from django.urls import include, re_path
from . import views
from notes import views as nt
urlpatterns = [
    re_path(r'^$', nt.home, name='home'),
    re_path(r'^register/$', views.signup, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]