from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    teacher = models.CharField(max_length=50)
    duration = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='lessons/')
    price = models.PositiveIntegerField()
    language = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
