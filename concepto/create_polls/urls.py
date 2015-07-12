from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^make_poll/', views.make_poll, name='make_poll'),
    url(r'^submit_poll/', views.submit_poll, name='submit_poll'),
]
