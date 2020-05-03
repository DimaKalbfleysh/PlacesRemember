from django.test import TestCase
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User

import datetime

from remember.models import (
	City,
	Remember,
)

# Create your tests here.
class CityTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		City.objects.create(name="Москва", people_population=10000000)

	def test_city_str_method(self):
		city=City.objects.get(id=1)
		expected_object_name = f"{city.name}"
		self.assertEquals(expected_object_name, str(city))


class RememberTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		city = City.objects.create(name="Москва", people_population=10000000)

		user = User.objects.create_user(username='testuser1', password='12345') 
		place = "Красная площадь"
		description = ""
		date = datetime.date.today()

		lng, lat = 55.7539303, 37.620795
		point = Point(lng, lat)

		Remember.objects.create(
			city=city,
			user=user,
			place=place,
			description=description,
			point=point,
			date=date,
		)

	def test_remember_str_method(self):
		remember=Remember.objects.get(id=1)
		expected_object_name = f"{remember.city}, {remember.place}"
		self.assertEquals(expected_object_name, str(remember))
