from django.test import TestCase
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User

import datetime

from remember.models import (
	City,
	Remember,
)
from remember.forms import (
	RememberForm,
)


class RememberFormTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		city = City.objects.create(name="Москва", people_population=10000000)

	def test_form_city_choices(self):
		form = RememberForm()
		form_city_choices = form.fields["city"].choices

		cities = City.objects.all().order_by("-people_population")
		expected_city_choices = []
		for city in cities:
			expected_city_choices.append((city.id, city.name))

		self.assertEquals(expected_city_choices, form_city_choices)

	def test_form_clean_method(self):
		city = City.objects.get(name="Москва")

		lng, lat = 55.7539303, 37.620795
		point = Point(lng, lat)

		form_data = {
			"city": city.id,
			"place": "Красная площадь",
			"description": "",
			"date": datetime.date.today(),
			"point": point,
		}
		form = RememberForm(data=form_data)
		self.assertTrue(form.is_valid())

		cleaned_data = form.cleaned_data
		extented_cleaned_data = {
			"city": city,
			"place": "Красная площадь",
			"description": "",
			"date": datetime.date.today(),
			"point": point,
		}
		self.assertEquals(extented_cleaned_data, cleaned_data)
