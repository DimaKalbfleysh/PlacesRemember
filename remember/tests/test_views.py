from django.test import TestCase
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.urls import reverse

import datetime

from remember.models import (
	City,
	Remember,
)


class RememberListViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		test_user1 = User.objects.create_user(username="testuser1", password="12345") 
		test_user1.save()
		current_site = Site.objects.get_current()
		fb = SocialApp.objects.create(
            provider="facebook",
            name="facebook",
            client_id="2582121902041764",
            secret="e2e61efc1b1b61ece6c9ca232601f877",
		)
		current_site.socialapp_set.add(fb)

		city = City.objects.create(name="Москва", people_population=10000000)
		place = "Красная площадь"
		description = ""
		date = datetime.date.today()

		lng, lat = 55.7539303, 37.620795
		point = Point(lng, lat)

		for i in range(3):
			Remember.objects.create(
				city=city,
				user=test_user1,
				place=place,
				description=description,
				point=point,
				date=date,
			)

	def test_not_login_redirect(self):
		resp = self.client.get(reverse("remember_list"))
		self.assertRedirects(resp, "/accounts/login/", status_code=302)

	def test_valid_url(self):
		login = self.client.login(username="testuser1", password="12345")
		resp = self.client.get("/remember/list/")
		self.assertEqual(resp.status_code, 200)

	def test_valid_reverse_url(self):
		login = self.client.login(username="testuser1", password="12345")
		resp = self.client.get(reverse("remember_list"))
		self.assertEqual(resp.status_code, 200)

	def test_valid_user(self):
		login = self.client.login(username="testuser1", password="12345")
		resp = self.client.get(reverse("remember_list"))
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(str(resp.context["user"]), "testuser1")

	def test_valid_template(self):
		login = self.client.login(username="testuser1", password="12345")
		resp = self.client.get(reverse("remember_list"))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, "remember/remember_list.html")

	def test_lists_user_remembers(self):
		login = self.client.login(username="testuser1", password="12345")
		resp = self.client.get(reverse("remember_list"))
		self.assertEqual(resp.status_code, 200)
		self.assertTrue(len(resp.context["remembers"]) == 3)


class RememberCreateViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		test_user1 = User.objects.create_user(username="testuser1", password="12345") 
		test_user1.save()
		current_site = Site.objects.get_current()
		fb = SocialApp.objects.create(
            provider="facebook",
            name="facebook",
            client_id="2582121902041764",
            secret="e2e61efc1b1b61ece6c9ca232601f877",
		)
		current_site.socialapp_set.add(fb)

		city = City.objects.create(name="Москва", people_population=10000000)
		place = "Красная площадь"
		description = ""
		date = datetime.date.today()

		lng, lat = 55.7539303, 37.620795
		point = Point(lng, lat)

		for i in range(3):
			Remember.objects.create(
				city=city,
				user=test_user1,
				place=place,
				description=description,
				point=point,
				date=date,
			)

	def test_not_login_redirect(self):
		resp = self.client.get(reverse("remember_create"))
		self.assertRedirects(resp, "/accounts/login/", status_code=302)

	def test_valid_url(self):
		login = self.client.login(username="testuser1", password="12345")
		resp = self.client.get("/remember/create/")
		self.assertEqual(resp.status_code, 200)

	def test_valid_reverse_url(self):
		login = self.client.login(username="testuser1", password="12345")
		resp = self.client.get(reverse("remember_create"))
		self.assertEqual(resp.status_code, 200)

	def test_valid_template(self):
		login = self.client.login(username="testuser1", password="12345")
		resp = self.client.get(reverse("remember_create"))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, "remember/remember_form.html")

	# def test_create_remember(self):
	# 	login = self.client.login(username='testuser1', password='12345')

	# 	city = City.objects.get(name="Москва")
	# 	place = "Красная площадь"
	# 	description = ""
	# 	date = datetime.date.today()

	# 	lng, lat = 55.7539303, 37.620795
	# 	point = Point(lng, lat)
	# 	create_data = {
	# 		"city": city.id,
	# 		"place": place,
	# 		"description": description,
	# 		"point": point,
	# 		"date": date
	# 	}
	# 	create_resp = self.client.post(reverse("remember_create"), create_data)
	# 	self.assertEqual(create_resp.status_code, 200)
	# 	list_resp = self.client.get(reverse('remember_list'))
	# 	self.assertTrue(len(list_resp.context['remembers']) == 4)
