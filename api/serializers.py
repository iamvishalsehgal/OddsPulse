from rest_framework import serializers
from .models import BettingSite, Match, Odds

class BettingSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BettingSite
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class OddsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odds
        fields = '__all__'
