from django.contrib import admin
from lessons.models import Lesson, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
class LessonAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'description', 'teacher',
                    'duration', 'slug', 'image',
                    'price', 'language', 'created_at']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Lesson, LessonAdmin)
