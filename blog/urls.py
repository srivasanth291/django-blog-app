from django.urls import path
from .views import (
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
    posts_by_category,
)

urlpatterns = [
    path('', post_list, name='post_list'),
    path('category/<slug:slug>/', posts_by_category, name='posts_by_category'),

    path('post/create/', post_create, name='post_create'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('post/<int:id>/edit/', post_update, name='post_update'),
    path('post/<int:id>/delete/', post_delete, name='post_delete'),
]
 