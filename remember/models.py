from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
	name = models.CharField(
		verbose_name="City name",
		max_length=32,
	)
	people_population = models.PositiveIntegerField(
		verbose_name="Population of people living in the city",
		default=0,
	)

	class Meta:
		verbose_name = 'City'
		verbose_name_plural = 'Cities'

	def __str__(self):
		return f"{self.name}"


class Remember(models.Model):
	user = models.ForeignKey(
		User,
		verbose_name="User own remember",
		on_delete=models.CASCADE,
	)
	city = models.ForeignKey(
		City,
		verbose_name="City of visit",
		on_delete=models.CASCADE,
	)
	place = models.CharField(
		verbose_name="Place of visit",
		max_length=512,
	)
	description = models.TextField(
		verbose_name="Description of remember",
		null=True,
	)
	date = models.DateField(
		verbose_name="Date of visit"
	)

	class Meta:
		verbose_name = 'Remember'
		verbose_name_plural = 'Remembers'

	def __str__(self):
		return f"{self.city.name}, {self.place}"