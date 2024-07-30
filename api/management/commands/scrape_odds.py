from django.core.management.base import BaseCommand
from api.scraper import fetch_odds_from_bet365, fetch_odds_from_unibet

class Command(BaseCommand):
    help = 'Scrapes odds from betting sites'

    def handle(self, *args, **kwargs):
        self.stdout.write('Fetching odds from bet365...')
        fetch_odds_from_bet365()
        self.stdout.write('Fetching odds from unibet...')
        fetch_odds_from_unibet()
        self.stdout.write('Done.')
