from django.db import models
from django.db.models import Model
from django.utils.timezone import now
from django.urls import reverse

# Create your models here.
class Player(models.Model):
	name = models.CharField(max_length=32)
	rating = models.IntegerField()

	def __str__(self):
		return f"Player Name: {self.name}, Player Rating: {self.rating}"

class Matchup(models.Model):
	player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player1")
	player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player2")
	p1Odds = models.IntegerField()
	dateCreated = models.DateTimeField(default=now, editable=False)

	def get_absolute_url(self):
		return reverse('matchup', kwargs={'pk': self.pk})


	def __str__(self):
		return f"{self.player1.name} has a {self.p1Odds}% chance of winning vs {self.player2.name}"