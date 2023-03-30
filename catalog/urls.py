from django.urls import path
from .views import (TaskCreateView,
                    TaskListView,
                    TaskUpdateView,
                    TaskDeleteView,
                    TagCreateView,
                    TagListView,
                    TagUpdateView,
                    TagDeleteView
                    )

urlpatterns = [

    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

    path("tag/", TagListView.as_view(), name="tag-list"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "to_do_list"