from atexit import register
from django.urls import path

from .import views

urlpatterns = [
    path('', views.Post_list,name='Post_list'),
    path('post_details<int:pk>/', views.post_details_page,name='post_details'),
    path('Post/new/',views.Post_new, name='Post_new'),
    path('Post/<int:pk>/edit/',views.Post_edit, name='Post_edit'),
    path('Post/<int:pk>/delete/',views.Post_delete,name='Post_delete'),
    path('register/',views.register_user,name='register_user'),
   
]