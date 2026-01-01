from django.urls import path
from .views import (
    post_list, post_detail,
    post_create, post_update, post_delete
)

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/create/', post_create, name='post_create'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('post/<int:id>/edit/', post_update, name='post_update'),
    path('post/<int:id>/delete/', post_delete, name='post_delete'),
]
