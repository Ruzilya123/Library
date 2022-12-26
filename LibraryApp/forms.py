from django import forms
from . import models


class ChoiceCategory(forms.Form):
    name = forms.ModelChoiceField(models.Category.objects)


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
        widgets = {
            'date_of_public' : forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }
