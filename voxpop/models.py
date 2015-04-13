from django.db import models

# Create your models here.
class Firm(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class Review(models.Model):
	#rev_id = models.IntgerField() //should we have this?
	firm = models.ForeignKey(Firm)
	role = models.CharField(max_length=128)
	salary = models.IntegerField(null=True)
	pros = models.CharField(max_length=300) # test/change this
	cons = models.CharField(max_length=300)
	estagio = models.CharField(max_length=300)

	def __unicode__(self):
		return "review " + str(self.id)