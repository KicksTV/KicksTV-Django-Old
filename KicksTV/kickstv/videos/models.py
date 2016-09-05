from django.db import models

# Create your models here.

class Playlist(models.Model):
	playlist_title = models.CharField(max_length=50)
	playlist_author = models.CharField(max_length=50)
	playlist_date = models.CharField(max_length=50)
	playlist_image = models.CharField(max_length=1500)
	playlist_description = models.CharField(max_length=300)

	def __str__(self):
		return self.playlist_title + ' - ' + self.playlist_author

class Video(models.Model):
	playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
	video_title = models.CharField(max_length=50)

	def __str__(self):
		return self.video_title