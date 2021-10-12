from card_app.API.serializers import CardSerializer
from rest_framework import viewsets

from card_app.models import Card


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
