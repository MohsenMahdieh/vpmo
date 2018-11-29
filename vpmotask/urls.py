from django.urls import path
from vpmotask.views import *

app_name = "vpmotask"

urlpatterns = [
	path(r"api/delete_update_create_task/", DeleteUpdateCreateTaskView.as_view(), name="delete_update_create_task"),
    path(r"api/assignable_task_users/<str:nodeID>/", AssignableTaskUsersView.as_view(), name="assignable_task_users"),
    path(r"api/list_assigned_tasks/<str:nodeID>/", AssignedTasksListView.as_view(), name="list_assigned_tasks"),

    path(r"api/scrumboard_task_list/", ScrumboardTaskListView.as_view(), name="scrumboard_task_list")
]