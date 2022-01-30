from django.urls import path 
from profiles.views import UpdateProfileView, DetailProfileView, ListProfileView, follow




urlpatterns = [
    path('update_profile/<slug:slug>/<int:pk>/', UpdateProfileView.as_view(), name='profile_update'),

    path('detail_profile/<slug:slug>/<int:pk>/', DetailProfileView.as_view(), name='profile_detail'),
    path('follow/<slug:slug>/<int:pk>/', follow, name='follow'),
    path('list_profile/', ListProfileView.as_view(), name='profile_list'),
]

