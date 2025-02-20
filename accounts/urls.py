from django.urls import path
from .views import login_view, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), 
    # Redirect to login page after logout
    path('livreur_home/', auth_views.LoginView.as_view(template_name='accounts/livreur_home.html'), name='livreur_home'),
]
