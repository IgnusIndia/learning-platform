from django.db import models



class Marks_obtained(models.Model):
	user_id = 
	physics = models.IntegerField()
	chemistry = models.IntegerField()
	maths = models.IntegerField()
	test_id = models.CharField()



	def __unicode__(self):
		return self.user_id    