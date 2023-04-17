from django.urls import path

from . import views

urlpatterns = [
	path("",views.ClassAPi.as_view(),name="class-api"),
	path("classes/",views.ClassView.as_view(),name = "class"),
	path("classes/<int:id>/",views.ClassView.as_view(),name = "class_detail"),
]