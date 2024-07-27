from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['category', 'title', 'description', 'teacher', 'duration', 'image', 'price']
