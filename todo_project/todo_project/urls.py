from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addTask/', add_task, name='addTask'),
    path('taskList/', task_list, name='taskList'),
    path('updateTask/<int:task_id>/', update_task, name='updateTask'),
    path('deleteTask/<int:task_id>/', delete_task, name='deleteTask'),
]
