from django.urls import path
from .views import (
    index,
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "catalog"

urlpatterns = [
    path("", index, name="index"),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "tasks/add/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag-list"
    ),
    path(
        "tags/add/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]
