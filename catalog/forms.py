from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "tags"]

        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "tags": forms.widgets.CheckboxSelectMultiple(),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }
