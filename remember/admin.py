from django.contrib import admin
from remember import models

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'people_population']
    list_filter = ['name', 'people_population']
    search_fields = ['name']


class RememberAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'place', 'date']
    list_filter = ['user', 'city', 'date']
    search_fields = ['user', 'city', 'place', 'description']


admin.site.register(models.City, CityAdmin)
admin.site.register(models.Remember, RememberAdmin)