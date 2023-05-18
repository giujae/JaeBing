from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list),
    path('post_create/', views.post_create),
    path('<int:post_pk>/', views.post_detail),
    path('post_delete_update/<int:post_pk>/', views.post_delete_update),

    path('<int:post_pk>/comments/', views.comment_list),
    path('<int:post_pk>/comment_create/', views.comment_create),
    path('<int:post_pk>/comment/<int:comment_pk>/', views.comment_update_delete),

]