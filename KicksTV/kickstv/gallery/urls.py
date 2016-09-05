from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='gallery'),
	url(r'^register/$', views.UserFormView.as_view(), name='register'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
	url(r'gallery/add/$', views.GalleryCreate.as_view(), name='gallery-add'),	
	url(r'(?P<pk>[0-9]+)/edit/$', views.GalleryUpdate.as_view(), name='gallery-update'),
	url(r'(?P<pk>[0-9]+)/delete/$', views.GalleryDelete.as_view(), name='gallery-delete'),

	url(r'image/add/$', views.ImageCreate.as_view(), name='image-add'),		
]

