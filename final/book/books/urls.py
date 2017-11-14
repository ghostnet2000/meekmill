from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'^detail/(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
  url(r'^delete/(?P<book_id>[0-9]+)/$',
      views.delete_book,
      name='delete_book'),
]
