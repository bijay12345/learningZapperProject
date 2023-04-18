from django.db import models


RESOURCE_TYPE = (
	("P","PDF"),
	("V","VIDEO"),
	)


class Class(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	lessons = models.ManyToManyField("Lesson",related_name = "classes")

	def __str__(self):
		return self.title

class Lesson(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	resources_count = models.IntegerField()
	resources = models.ManyToManyField('Resources',related_name="lessons")

	def __str__(self):
		return self.title

class Resources(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	resource_type= models.CharField(max_length = 2,choices = RESOURCE_TYPE)

	def __str__(self):
		return self.title

	class Meta:
		indexes = [
			models.Index(fields=['resource_type']),
		]
