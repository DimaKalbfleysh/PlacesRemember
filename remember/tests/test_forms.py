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

	def get_default_valid_form_data(self):
		city = City.objects.get(name="Москва")

		lng, lat = 55.7539303, 37.620795
		point = Point(lng, lat)

		form_data = {
			"city": city.id,
			"place": "Красная площадь",
			"date": datetime.date.today(),
			"description": "Красивое место",
			"point": point,
		}
		return form_data

	def test_fields_form(self):
		form = RememberForm()

		form_fields = list(form.fields.keys())
		expected_form_fields = [
			"city",
			"place", 
			"description", 
			"date", 
			"point", 
		]
		self.assertEquals(expected_form_fields, form_fields)

	def test_form_city_choices(self):
		form = RememberForm()
		form_city_choices = form.fields["city"].choices

		cities = City.objects.all().order_by("-people_population")
		expected_city_choices = []
		for city in cities:
			expected_city_choices.append((city.id, city.name))

		self.assertEquals(expected_city_choices, form_city_choices)

	def test_valid_form_without_description(self):
		form_data = self.get_default_valid_form_data()
		form_data.pop("description")
		form = RememberForm(data=form_data)
		self.assertTrue(form.is_valid())

	def test_invalid_form_without_place(self):
		form_data = self.get_default_valid_form_data()
		form_data.pop("place")
		form = RememberForm(data=form_data)
		self.assertFalse(form.is_valid())

	def test_invalid_form_without_date(self):
		form_data = self.get_default_valid_form_data()
		form_data.pop("date")
		form = RememberForm(data=form_data)
		self.assertFalse(form.is_valid())

	def test_invalid_form_without_point(self):
		form_data = self.get_default_valid_form_data()
		form_data.pop("point")
		form = RememberForm(data=form_data)
		self.assertFalse(form.is_valid())

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
