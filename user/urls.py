from django.urls import path 
from django.contrib.auth.views import LogoutView
from user.views import register, update_user, login, UpdateUserView




urlpatterns = [
     path('register/', register, name='register'),
     path('update_user/', update_user, name='update_user'),
     path('login/', login, name='login'),
     path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
     path('update_user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
     path('password_change/', update_user, name='password_change'),
     
]
