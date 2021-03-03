from django.urls import path

from . import views

urlpatterns = [
    path('screen/', views.screen, name='color_tool_screen'),
]
