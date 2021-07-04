from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  
    url(r'^$',views.gallery,name='gallery'),
    url(r'^galllery$',views.my_gallery,name='myGallery'),
    url(r'^search/', views.search_images,name = 'search_images'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'location/(?P<location>\w+)',views.locations,name = 'location'),

    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
