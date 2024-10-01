from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4, "cols": 40}),
        }

