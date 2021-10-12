from rest_framework import serializers
from card_app.models import *


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['name', 'surname', 'photo', 'country', 'city', 'avenue', 'phone_number']

    def validate(self, data):
        name = Card.objects.filter(name=data['name'], surname=data['surname'])
        if name:
            raise serializers.ValidationError("This combination of name and surname already created")
        return data
