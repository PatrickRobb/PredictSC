from django.urls import path
from scodds.views import MatchupListView, MatchupDetailView, PlayerListView, PlayerDetailView
from . import views

urlpatterns = [
	#path("", views.index, name="index"),
	path('', MatchupListView.as_view(), name='index'),
	path("<int:pk>", MatchupDetailView.as_view(), name="matchup"),
	path("players/<int:pk>", PlayerDetailView.as_view(), name="player"),
	path("players", PlayerListView.as_view(), name="players"),
	# path("players", views.players, name="players"),
	#path("<int:matchup_id>", views.matchuppage, name="matchup"),
	#path("predict", views.predict, name="predict")
]