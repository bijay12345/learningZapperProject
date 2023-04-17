from django.shortcuts import render
from django.http import HttpResponse
from .models import Class,Lesson,Resources
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClassSerializer,ResourceSerializer,LessonSerializer
from rest_framework.renderers import TemplateHTMLRenderer

class ClassAPi(APIView):
	def get(self,request,format=None):
		data = Class.objects.all()
		serializer = ClassSerializer(data,many=True)
		return Response({"data":serializer.data})

class ClassView(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	def get(self,request,id=None,format=None):
		if id is not None:
			c = Class.objects.get(id=id)
			serializer= ClassSerializer(c)
			return Response({"classes":serializer.data},template_name = "main/detail.html")
		data = Class.objects.all()
		serializer = ClassSerializer(data,many=True)
		return Response({"data":serializer.data},template_name = "main/home.html")

