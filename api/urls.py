from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BettingSiteViewSet, MatchViewSet, OddsViewSet

router = DefaultRouter()
router.register(r'bettingsites', BettingSiteViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'odds', OddsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
