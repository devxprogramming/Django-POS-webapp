from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='home'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('user-profile/<pk>', views.UserProfileDetail.as_view(), name='user_profile'),
]
