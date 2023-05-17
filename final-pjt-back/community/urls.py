from django.urls import path
from . import views

urlpatterns = [
    # community
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:board_pk>/', views.detail, name='detail'),
    path('update_delete/<int:board_pk>/', views.update_delete, name='update_delete'),
    
    # comment
    path('<int:board_pk>/comments/', views.comment_list, name='comment_list'),
    path('<int:board_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:board_pk>/comment/<int:comment_pk>/', views.comment_update_delete, name='comment_update_delete'),
]