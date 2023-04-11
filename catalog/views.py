from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


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


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "catalog/task_confirm_delete.html"
    success_url = reverse_lazy("catalog:task-list")


class TagCreateView(CreateView):
    model = Tag
    fields = ["name"]
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag_list")


class TagListView(ListView):
    model = Tag
    template_name = "catalog/tag_list.html"
    context_object_name = "tags"


class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "catalog/tag_form.html"
    success_url = reverse_lazy("catalog:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "catalog/tag_confirm_delete.html"
    success_url = reverse_lazy("catalog:tag-list")


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "catalog/tag_list.html", {"tags": tags})


@login_required
def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag-list")
    else:
        form = TagForm()
    return render(request, "catalog/tag_form.html", {"form": form})


def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("catalog:tag-detail", pk=pk)
    else:
        form = TagForm(instance=tag)
    return render(request, "catalog/tag_update.html", {"form": form})


@login_required
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        messages.success(request, "Tag has been deleted!")
        return redirect("catalog:tag-list")


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "catalog/task_list.html", {"tasks": tasks})


@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect("catalog:task-list")
    return render(request, "catalog/task_create.html", {"form": form})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "catalog/task_detail.html", {"task": task})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("catalog:task_detail", pk=pk)
    return render(request, "catalog/task_form.html", {"form": form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task has been deleted!")
        return redirect("catalog:task-list")
    return render(
        request,
        "catalog/task_confirm_delete.html",
        {"object": task}
    )


@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.completed_date = timezone.now()
    task.save()
    messages.success(
        request,
        f"Task '{task.content}' has been marked as complete!"
    )
    return redirect("task-list")
