from django.contrib import admin
from scodds.models import Player, Matchup
# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")

class MatchupAdmin(admin.ModelAdmin):
    list_display = ("id", "player1", "player2", "bestOf", "p1Odds", "p1AligulacOdds", "kellyValue", "matchupDate")

admin.site.register(Player, PlayerAdmin)
admin.site.register(Matchup, MatchupAdmin)