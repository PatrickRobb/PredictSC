from django.db import models
from django.db.models import Model
from django.utils.timezone import now
from django.urls import reverse
import requests
import json
from datetime import date


player_list = {
  "Serral": 485,
  "Maru": 49,
  "Reynor": 5414,
  "Dark": 76,
  "Parting": 5,
  "Cure": 1665
}

# Create your models here.
class Player(models.Model):
	name = models.CharField(max_length=32)
	country = models.CharField(max_length=32, default = "N/A")
	#age = models.IntegerField(default= 0)

	def save(self, *args, **kwargs):
		response = requests.get("http://aligulac.com/api/v1/player/" + str(player_list[self.name]) + "/?apikey=iSvLFUXkHGQFk1sTLCZo")
		responseJSON = response.json()
		self.country = responseJSON["country"]
		#self.age = responseJSON["age"]
		super(Player, self).save(*args, *kwargs)

	def __str__(self):
		return f"Player name: {self.name}, Player nationality: {self.country}"

class Matchup(models.Model):
	player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player1")
	player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player2")
	bestOf = models.IntegerField(default= 3)
	p1Odds = models.FloatField(default = 0)
	p1AligulacOdds = models.FloatField(default = 0)
	kellyValue = models.FloatField(default = 0)
	matchupDate = models.DateField(default = date.today)

	def get_absolute_url(self):
		return reverse('matchup', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):
		response = requests.get("http://aligulac.com/api/v1/predictmatch/" + str(player_list[self.player1.name]) + "," + str(player_list[self.player2.name]) + "/?apikey=iSvLFUXkHGQFk1sTLCZo&bo="+str(self.bestOf))
		responseJSON = response.json()
		self.p1AligulacOdds = responseJSON['proba']*100
		self.kellyValue = ((((1/(self.p1Odds/100)-1)*responseJSON['proba'])-(1-responseJSON['proba']))/(1/(self.p1Odds/100)-1))
		super(Matchup, self).save(*args, *kwargs)

	def __str__(self):
		return f"The given odds say {self.player1.name} has a {self.p1Odds}% chance of winning vs {self.player2.name}. Aligulac odds say {self.player1.name} has a {self.p1AligulacOdds}% chance of winning. According to the Kelly Criterion, you should bet {self.kellyValue * 100}%"

			# @property
	# def p1AligulacOdds(self):
	# 	response = requests.get("http://aligulac.com/api/v1/predictmatch/" + str(player_list[self.player1.name]) + "," + str(player_list[self.player2.name]) + "/?apikey=iSvLFUXkHGQFk1sTLCZo&bo="+str(self.best_of))
	# 	responseJSON = response.json()
	# 	return responseJSON['proba']*100
	
	# @property
	# def kellyValue(self):
	# 	response = requests.get("http://aligulac.com/api/v1/predictmatch/" + str(player_list[self.player1.name]) + "," + str(player_list[self.player2.name]) + "/?apikey=iSvLFUXkHGQFk1sTLCZo&bo="+str(self.best_of))
	# 	responseJSON = response.json()
	# 	return (((self.p1Odds*responseJSON['proba'])-(1-responseJSON['proba']))/self.p1Odds)
    
	# @property
    # def p1AligulacOdds(self):
    #      return self.p1Odds
    