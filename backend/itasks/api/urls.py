from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks),
    path('createtask/', views.add_task),
    path('tasks/<int:id>/', views.get_user_tasks),

    path('tasks/<int:id>/update/', views.update_task),
    path('tasks/<int:id>/delete/', views.delete_task),

    path('users/', views.get_users),
    path('createuser/', views.add_user),
]
