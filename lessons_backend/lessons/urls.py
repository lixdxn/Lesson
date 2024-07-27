from django.urls import path

from .views import LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView, LessonDeleteView


urlpatterns = [
    path('', LessonListView.as_view(), name='lesson_list'),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),
    path('<slug:slug>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('<slug:slug>/edit/', LessonUpdateView.as_view(), name='lesson_update'),
    path('<slug:slug>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
]
