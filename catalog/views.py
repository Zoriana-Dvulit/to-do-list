from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Task, Tag

# Task views


class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "description", "due_date", "completed", "tags"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy('task-list')


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = 'tasks'


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "description", "due_date", "completed", "tags"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy('task-list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task-list")


# Tag views

class TagCreateView(CreateView):
    model = Tag
    fields = ["name"]
    template_name = "tags/tag_form.html"
    success_url = reverse_lazy("tag-list")


class TagListView(ListView):
    model = Tag
    template_name = "tags/tag_list.html"
    context_object_name = "tags"


class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "tags/tag_form.html"
    success_url = reverse_lazy("tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags/tag_confirm_delete.html"
    success_url = reverse_lazy("tag-list")
