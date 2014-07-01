from django.db import models


class student(models.Model):
	student_id = models.IntegerField(blank=False)
	name = models.CharField(max_length=100, blank=False)
	dob = models.DateField()
	doj = models.DateField()


	def __unicode__(self):
		return self.student_id


class Subject(models.Model):
	subject_id = models.CharField(max_length=100)

	def __unicode__(self):
		return self.student_id

