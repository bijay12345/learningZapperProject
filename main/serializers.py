from rest_framework.serializers import ModelSerializer
from .models import Class,Lesson,Resources

class ResourceSerializer(ModelSerializer):
	class Meta:
		model = Resources 
		fields = ["id","title","description","resource_type"]

	def get_queryset(self):
		qs=super().get_queryset()
		result=qs.values("resource_type")
		return result


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