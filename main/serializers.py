from rest_framework.serializers import ModelSerializer
from .models import Class,Lesson,Resources
from rest_framework import filters

class ResourceSerializer(ModelSerializer):
	class Meta:
		model = Resources 
		fields = ["title","description","resource_type"]
		filter_backends = [filters.OrderingFilter]
		ordering_fields = 'resource_type'


class LessonSerializer(ModelSerializer):
	resources = ResourceSerializer(read_only=True,many=True)
	class Meta:
		model = Lesson 
		fields = "__all__"


class ClassSerializer(ModelSerializer):
	lessons=LessonSerializer(read_only=True,many=True)
	class Meta:
		model = Class 
		fields = '__all__'