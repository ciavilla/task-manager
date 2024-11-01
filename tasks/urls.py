from django.urls import path
from .views import create_task, show_my_tasks, update_task_status

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("<int:task_id>/", update_task_status, name="update_task_status"),
]
