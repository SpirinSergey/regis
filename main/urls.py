from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('developers', views.developers, name='developers'),
    path('amenities', views.amenities, name='amenities'),
    path('gallery', views.gallery, name='gallery'),
    path('listings', views.listings, name='listings'),
    path('contact', views.contact, name='contact'),
    path('privacy-policy', views.privacy, name='privacy-policy'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    ]