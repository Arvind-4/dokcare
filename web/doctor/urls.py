from django.urls import path

from .views import (
    HomeView,
    BlogView,
    ContactView,
    DoctorView,
    FaqView,
    GalleryView,
    ServiceView,
)

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('blog/',BlogView.as_view(), name='blog'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('doctors/',DoctorView.as_view(), name='doctors'),
    path('faq/',FaqView.as_view(), name='faq'),
    path('gallery/',GalleryView.as_view(), name='gallery'),
    path('services/',ServiceView.as_view(), name='services'),
]