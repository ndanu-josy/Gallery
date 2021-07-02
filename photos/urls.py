from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  
    url(r'^$',views.home,name='home'),
    url(r'^galllery$',views.my_gallery,name='myGallery'),
    url(r'^search/', views.search_images,name = 'search_images'),
    
    

]