from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic import CreateView

from .models import Task, Tag
from .forms import TagForm, TaskForm


@login_required
def index(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "catalog/index.html", context)


class TaskCreateView(CreateView):
    model = Task
    fields = ["description", "created_date", "due_date", "done", "tags"]
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:task-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "catalog/task_list.html"
    context_object_name = "tasks"


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = "catalog/task_detail.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "due_date", "done", "tags"]
    template_name = "catalog/task_update.html"
    success_url = reverse_lazy("catalog:task-list")

    def form_valid(self, form):
        form.instance.updated_date = timezone.now()
        return super().form_valid(form)


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "catalog/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag_list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    context_object_name = "tags"


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "catalog/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")


class TaskCompleteView(generic.View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        task.completed = True
        task.completed_date = timezone.now()
        task.save()
        messages.success(request, f"Task '{task.content}' has been marked as complete!")
        return redirect("catalog:task-list")


class TaskCreateByUserView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateByUserView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "catalog/task_form.html"
    success_url = reverse_lazy("catalog:task-list")

    def get_queryset(self):
        return super().get
