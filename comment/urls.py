from django.urls import path 
from comment.views import (
    createCommentView,
    deleteCommentView
)


urlpatterns = [
    path('create_comment/<slug:slug>/<int:pk>/', createCommentView, name='create_comment'),
    
    path('delete_comment/<slug:slug>/<int:pk>/', deleteCommentView, name='delete_comment')
]
