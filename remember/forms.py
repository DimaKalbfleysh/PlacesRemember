from django import forms

from remember import models


class RememberForm(forms.ModelForm):
    city = forms.ChoiceField(label="Выбрать город", required=True)
    place = forms.CharField(max_length=512, label="Место", required=True)
    description = forms.CharField(widget=forms.Textarea, label="Описание", required=False)
    date = forms.DateField(widget=forms.SelectDateWidget, label="Дата", required=True)

    class Meta:
        model = models.Remember
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["city"].choices = self.get_cities_choice()

    def get_cities_choice(self):
        cities = models.City.objects.all().order_by("-people_population")
        return (
            (city.id, city.name) 
            for city in cities
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        city_id = cleaned_data.pop("city")
        city = models.City.objects.get(pk=city_id)
        cleaned_data["city"] = city
        return cleaned_data