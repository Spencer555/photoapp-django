from django.urls import path 
from photos.views import (
    CreatePhotoView,
    likePhoto,
    dislikePhoto,
    DeletePhotoView,
    DetailPhotoView,
    ListPhotoView,
    UpdatePhotoView,
    SearchView
    
)


urlpatterns = [
    path('like_photo/<slug:slug>/<int:pk>/', likePhoto, name='like_photo'),
    
    path('dislike_photo/<slug:slug>/<int:pk>/', dislikePhoto, name='dislike_photo'),

    path('create_photo/', CreatePhotoView.as_view(), name='create_photo'),
    
    path('', ListPhotoView.as_view(), name='list_photo'),

    path('detail_photo/<slug:slug>/<int:pk>/', DetailPhotoView.as_view(), name='detail_photo'),

    path('update_photo/<slug:slug>/<int:pk>/', UpdatePhotoView.as_view(), name='update_photo'),

    path('delete_photo/<slug:slug>/<int:pk>/', DeletePhotoView.as_view(), name='delete_photo'),

]

