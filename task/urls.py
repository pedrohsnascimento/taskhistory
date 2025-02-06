from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_task, name='list_task'),
    path('add/', views.add_task, name='add_task'),
    path('att/<int:task_id>/', views.att_task, name='att_task'),
    path('del/<int:task_id>/', views.del_task, name='del_task'),
    path('ver/<int:task_id>/', views.ver_task, name='ver_task'),

]
