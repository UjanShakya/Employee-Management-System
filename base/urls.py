from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexPage, name='index'),
    path('viewall/', views.viewallPage, name='viewall'),

    path('add/', views.addPage, name='add'),
    path('search', views.searchPage, name='search'),
    path('delete/', views.deletePage, name='delete'),

    path('delete/<int:pk>', views.deletePage, name='delete'),



]
