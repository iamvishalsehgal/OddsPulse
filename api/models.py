from django.db import models

class BettingSite(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class Match(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}"

class Odds(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    betting_site = models.ForeignKey(BettingSite, on_delete=models.CASCADE)
    home_odds = models.DecimalField(max_digits=5, decimal_places=2)
    draw_odds = models.DecimalField(max_digits=5, decimal_places=2)
    away_odds = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Odds for {self.match} on {self.betting_site}"
