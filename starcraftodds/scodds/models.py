from django.db import models
from django.db.models import Model
from django.utils.timezone import now
from django.urls import reverse
import requests
import json
from datetime import date
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

aligulac_key_list = {
    "Serral": 485, "Maru": 49, "Reynor": 5414, "Dark": 76, "Parting": 5, "Cure": 1665,
    "herO": 233, "Clem": 5878, "MaxPax": 19591, "ByuN": 47, "Rogue": 1662, "Bunny": 1517,
    "HeRoMaRinE": 258, "Zest": 1658, "Solar": 1793, "ShoWTimE": 2170, "Neeb": 4495,
    "Elazer": 5847, "Astrea": 4134, "RagnaroK": 117, "DRG": 4, "Trap": 177, "GuMiho": 44,
    "Lambo": 4049, "Zoun": 2053, "soO": 125, "Creator": 2, "TIME": 10115, "SKillous": 8676,
    "Classic": 186, "Dream": 109, "SpeCial": 184, "Scarlett": 23, "uThermal": 575,
    "Spirit": 4452, "Ryung": 35, "Harstem": 214, "KeeN": 24, "Denver": 4564, "Gerald": 8913,
}

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=32)
    full_name = models.CharField(max_length=32, default="N/A")
    country = models.CharField(max_length=32, default="N/A")
    #age = models.IntegerField(default= 0)

    def save(self, *args, **kwargs):
        response = requests.get("http://aligulac.com/api/v1/player/" + str(
            aligulac_key_list[self.name]) + "/?apikey=" + os.environ['MY_ALIGULAC_KEY'])
        responseJSON = response.json()
        self.country = responseJSON["country"]
        self.full_name = responseJSON["name"]
        super(Player, self).save(*args, *kwargs)

    def __str__(self):
        return f"Player name: {self.name}, Player nationality: {self.country}"


class Matchup(models.Model):
    player1 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="player1")
    player2 = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="player2")
    bestOf = models.IntegerField(default=3)
    p1Odds = models.FloatField(default=0)
    p1AligulacOdds = models.FloatField(default=0)
    kellyValue = models.FloatField(default=0)
    matchupDate = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('matchup', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        response = requests.get("http://aligulac.com/api/v1/predictmatch/" + str(aligulac_key_list[self.player1.name]) + "," + str(
            aligulac_key_list[self.player2.name]) + "/?apikey=" + os.environ['MY_ALIGULAC_KEY'] + "&bo=" + str(self.bestOf))
        responseJSON = response.json()
        self.p1AligulacOdds = responseJSON['proba']*100
        self.kellyValue = ((((1/(self.p1Odds/100)-1)*responseJSON['proba'])-(1-responseJSON['proba']))/(
            1/(self.p1Odds/100)-1))  # This is the Kelly formula: K=(P*B-(1-P))/B
        super(Matchup, self).save(*args, *kwargs)

    def __str__(self):
        return f"The given odds say {self.player1.name} has a {self.p1Odds}% chance of winning vs {self.player2.name}. Aligulac odds say {self.player1.name} has a {self.p1AligulacOdds}% chance of winning. According to the Kelly Criterion, you should wager {self.kellyValue * 100}% of your bankroll."
