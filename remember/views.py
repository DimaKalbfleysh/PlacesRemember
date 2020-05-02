from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView,
)
from django.urls import reverse

from remember import models
from remember import forms


class RememberViewMixin():
	form_class = forms.RememberForm
	model = models.Remember

	def form_valid(self, form):
	    form.instance.user = self.request.user
	    return super().form_valid(form)

	def get_success_url(self):
	    return reverse("remember_list")


class RememberList(RememberViewMixin, ListView):
	template_name = "remember/remember_list.html"
	context_object_name = "remembers"

	def get_queryset(self):
		user = self.request.user
		remembers = self.model.objects.filter(
			user=user
		)
		return remembers


class RememberDetail(RememberViewMixin, DeleteView):
	template_name = "remember/remember_detail.html"


class RememberCreate(RememberViewMixin, CreateView):
	template_name = "remember/remember_form.html"


class RememberUpdate(RememberViewMixin, UpdateView):
	template_name = "remember/remember_form.html"


class RememberDelete(RememberViewMixin, DeleteView):
	pass
