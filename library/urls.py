from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='library_home'),
    path('legacy/', views.legacy, name='legacy'),
]
