from django.urls import path
from scodds.views import  MatchupDetailView, PlayerListView, MatchupCreateView
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	#path('', MatchupListView.as_view(), name='index'),
	path("matchup/<int:pk>", MatchupDetailView.as_view(), name="matchup"),
	path("players/<int:player_id>", views.playerpage, name="player"),
	#path("players/<int:pk>", PlayerDetailView.as_view(), name="player"),
	path("players", PlayerListView.as_view(), name="players"),
	path("matchup/new", MatchupCreateView.as_view(), name = "matchup-create")
	# path("players", views.players, name="players"),
	#path("<int:matchup_id>", views.matchuppage, name="matchup"),
	#path("predict", views.predict, name="predict")
]