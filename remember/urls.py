from django.urls import path, include
from remember import views

urlpatterns = [
	path('list/', views.remember_list, name='remember_list'),
]
