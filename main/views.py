from django.shortcuts import render
from .models import Class,Lesson,Resources
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClassSerializer,ResourceSerializer,LessonSerializer
from rest_framework.renderers import TemplateHTMLRenderer

class ClassAPi(APIView):
	def get(self,request,format=None):
		data = Class.objects.all().prefetch_related("lessons","lessons__resources")
		serializer = ClassSerializer(data,many=True)
		return Response({"data":serializer.data})


class ClassView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	def get(self,request,id=None,format=None):
		if id is not None:
			c = Class.objects.prefetch_related("lessons","lessons__resources").get(id=id)
			serializer= ClassSerializer(c)
			return Response({"data":serializer.data},template_name = "main/detail.html")
		
		data = Class.objects.all().prefetch_related("lessons","lessons__resources")
		serializer = ClassSerializer(data,many=True)
		return Response({"data":serializer.data},template_name = "main/home.html")
