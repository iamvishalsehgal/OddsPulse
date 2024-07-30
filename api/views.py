from rest_framework import viewsets
from .models import BettingSite, Match, Odds
from .serializers import BettingSiteSerializer, MatchSerializer, OddsSerializer

class BettingSiteViewSet(viewsets.ModelViewSet):
    queryset = BettingSite.objects.all()
    serializer_class = BettingSiteSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class OddsViewSet(viewsets.ModelViewSet):
    queryset = Odds.objects.all()
    serializer_class = OddsSerializer
