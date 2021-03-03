from django.urls import include, path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.signout, name='logout'),
    path('registration', views.registration, name='registration'),
    path('manual', views.manual, name='manual'),
    path('form16', views.form16, name='form16'),
    path('oauth/', include('social_django.urls', namespace='social')), 
    path('<str:username>', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)