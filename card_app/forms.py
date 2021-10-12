from django.forms import ModelForm
from .models import *
from django import forms


class CardCreateForm(ModelForm):

    class Meta:
        model = Card
        fields = ('photo', 'name', 'surname', 'country', 'city', 'avenue', 'phone_number')

    def clean(self):
        clean_data = super().clean()
        name = Card.objects.filter(name=clean_data.get('name'), surname=clean_data.get('surname'))
        if name:
            raise forms.ValidationError('This name already created!')
