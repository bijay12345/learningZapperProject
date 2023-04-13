from django.contrib import admin
from .models import Class,Lesson,Resources

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
	list_display = ['title','description']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
	list_display = ['title','description','resources_count']

@admin.register(Resources)
class ResourceAdmin(admin.ModelAdmin):
	list_display = ['title','description',"resource_type"]