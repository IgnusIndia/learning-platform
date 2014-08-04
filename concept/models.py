from django.db import models
from autoslug.fields import AutoSlugField


class Concept(models.Model):
	SUB_CHOICES = (
           ('1', 'Physics'),
           ('2', 'Chemistry'),
           ('3', 'Maths'),
         )
	title = models.CharField(max_length=100)
	video_url = models.URLField(null=False)
	description = models.TextField()
	example = models.TextField()
	notes = models.TextField()
	subject = models.CharField(max_length=100, choices=SUB_CHOICES)
	slug = AutoSlugField(populate_from=('title'))
	



	def __unicode__(self):
		return self.title





		 