from django.urls import path

from tasks.views import tasks, task_detail

urlpatterns = [
    path("tasks/", view=tasks),
    path("tasks/<int:pk>/", view=task_detail)
]
