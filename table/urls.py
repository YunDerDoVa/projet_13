from django.urls import path

from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.post, name='post'),
    path('publish/', views.publish, name='publish'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
]