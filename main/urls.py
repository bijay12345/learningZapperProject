from django.urls import path

from . import views

urlpatterns = [
	path("classes/",views.ClassView.as_view(),name = "class"),
	path("classes/<int:id>/",views.ClassView.as_view(),name = "class_detail"),
]