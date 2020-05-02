from django.urls import path, include
from remember import views

urlpatterns = [
	path("list/", views.RememberList.as_view(), name='remember_list'),
	path("create/", views.RememberCreate.as_view(), name='remember_create'),
	path("<int:pk>/update/", views.RememberUpdate.as_view(), name='remember_update'),
	path("<int:pk>/delete/", views.RememberDelete.as_view(), name='remember_delete'),
]
