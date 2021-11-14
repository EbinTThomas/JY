from . import views
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]