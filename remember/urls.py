from django.urls import path, include
from remember import views

urlpatterns = [
	path('list/', views.RememberList.as_view(), name='remember_list'),
	path('create/', views.RememberCreate.as_view(), name='remember_create'),
]
