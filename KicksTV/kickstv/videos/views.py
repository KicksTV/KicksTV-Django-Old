from django.http import HttpResponse
from .models import Playlist

from django.views import generic


class IndexView(generic.ListView):
	template_name = 'videos/index.html'
	context_object_name = 'all_playlists'

	def get_queryset(self):
		return Playlist.objects.all()