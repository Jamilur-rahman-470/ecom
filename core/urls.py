
from django.urls import path
from . import views

urlpatterns = [
    path('user/sign-in', views.login_user, name='login'),
    path('user/sign-up', views.register_user, name='register'),
    path('user/logout', views.logout_user, name='logout'),
    path('user/dashboard', views.user_dashboard, name='dash'),
    path('user/update-profile', views.profile_update, name='user.profile.update'),
    path('user/update-address', views.address_update, name='user.address.update')
]
