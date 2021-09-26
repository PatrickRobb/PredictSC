from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Matchup
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.detail import DetailView
# from django.views.generic.create import CreateView
# Create your views here.

def index(request):
	return render(request, "scodds/index.html", {
		"matchups": Matchup.objects.order_by('-dateCreated')
		})

class MatchupListView(ListView):

    model = Matchup
    paginate_by = 100  # if pagination is desired
    template_name = 'scodds/index.html'
    context_object_name = 'matchups'
    oddering = ['-dateCreated']

class MatchupDetailView(DetailView):

    model = Matchup
    template_name = 'scodds/matchup.html'
    context_object_name = 'matchup'

class MatchupCreateView(LoginRequiredMixin, CreateView):
	model = Matchup
	fields =['player1', 'player2', 'p1Odds',]

class PlayerListView(ListView):

    model = Player
    paginate_by = 100  # if pagination is desired
    template_name = 'scodds/players.html'
    context_object_name = 'players'

class PlayerDetailView(DetailView):

    model = Player
    template_name = 'scodds/playerpage.html'
    context_object_name = 'player' 

# def playerpage(request, player_id):
# 	player = Player.objects.get(pk=player_id)
# 	return render(request, "scodds/playerpage.html", {
# 		"player": player
# 		})

# def players(request):
# 	players = Player.objects.all()
# 	return render(request, "scodds/players.html", {
# 		"players": players
# 		})

# def matchuppage(request, matchup_id):
# 	matchup = Matchup.objects.get(pk=matchup_id)
# 	return render(request, "scodds/matchup.html", {
# 		"matchup": matchup
# 		})

def predict(request):
	return render(request, "scodds/predict.html")