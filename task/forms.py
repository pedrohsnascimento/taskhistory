from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
