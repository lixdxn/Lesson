from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Lesson
from .forms import LessonForm
from .messages import ErrorMessages


class LessonListView(ListView):
    model = Lesson
    template_name = 'lessons/lesson_list.html'
    context_object_name = 'lessons'


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lessons/lesson_detail.html'
    context_object_name = 'lesson'


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lessons/lesson_form.html'
    success_url = reverse_lazy('lesson_list')

    def form_valid(self, form):
        # Check if a lesson with the same title or slug already exists
        title = form.cleaned_data['title']
        slug = form.cleaned_data['slug']

        if Lesson.objects.filter(title=title).exists() or Lesson.objects.filter(slug=slug).exists():
            messages.error(self.request, ErrorMessages.COURSE_ALREADY_EXISTS)
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, ErrorMessages.INVALID_FORM_DATA)
        return super().form_invalid(form)


class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lessons/lesson_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('lesson_list')

    def form_valid(self, form):
        # Check if a lesson with the same title or slug already exists
        title = form.cleaned_data['title']
        slug = form.cleaned_data['slug']

        if Lesson.objects.filter(title=title).exclude(pk=self.object.pk).exists() or \
                Lesson.objects.filter(slug=slug).exclude(pk=self.object.pk).exists():
            messages.error(self.request, ErrorMessages.COURSE_ALREADY_EXISTS)
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, ErrorMessages.INVALID_FORM_DATA)
        return super().form_invalid(form)


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'lessons/lesson_confirm_delete.html'
    success_url = reverse_lazy('lesson_list')

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, 'Lesson deleted successfully.')
            return response
        except Exception:
            messages.error(request, ErrorMessages.DELETE_ERROR)
            return redirect(self.success_url)
