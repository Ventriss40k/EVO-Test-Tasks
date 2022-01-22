from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_all/', views.show_all, name='show_all'),
]