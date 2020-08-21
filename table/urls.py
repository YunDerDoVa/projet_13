from django.urls import path

from . import views
from . import ajax

urlpatterns = [
    path('post/<int:post_id>/', views.post, name='table_post'),
    path('publish/', views.publish, name='table_publish'),
    path('edit/<int:post_id>/', views.edit, name='table_edit'),
    path('like/<int:post_id>/<int:like_from_id>/', ajax.like_post, name='like_post'),
    path('dislike/<int:post_id>/<int:like_from_id>/', ajax.dislike_post, name='dislike_post'),
]
