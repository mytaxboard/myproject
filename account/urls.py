from django.urls import include, path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.signout, name='logout'),
    path('registration', views.registration, name='registration'),
    path('manual', views.manual, name='manual'),
    path('form16', views.form16, name='form16'),
    path('<str:username>', views.profile, name='profile'),
]