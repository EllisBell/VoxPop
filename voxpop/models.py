from django.db import models

# Create your models here.
class Firm(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class Review(models.Model):
	#rev_id = models.IntgerField() //should we have this?
	firm = models.ForeignKey(Firm)
	tagline = models.CharField(max_length=140)
	rating = models.IntegerField()
	role = models.CharField(max_length=100)
	salary = models.IntegerField(null=True)
	pros = models.CharField(max_length=1000) # test/change this
	cons = models.CharField(max_length=1000)
	estagio = models.CharField(max_length=1000)
	dt = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "review " + str(self.id)