from django.urls import path
from .views import home, profile, RegisterView,custom_logout_view
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('logout/', custom_logout_view, name='logout'),

]
