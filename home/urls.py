from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pricing', views.pricing, name='pricing'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contactus', views.contactus, name='contactus'),
]