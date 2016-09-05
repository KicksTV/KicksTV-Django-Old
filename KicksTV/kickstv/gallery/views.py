from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm

from .models import Gallery
from .models import Image


class IndexView(generic.ListView):
	template_name = 'gallery/index.html'
	context_object_name = 'all_gallerys'

	def get_queryset(self):
		return Gallery.objects.all()


class DetailView(generic.DetailView):
	model = Gallery
	template_name = 'gallery/detail.html'



class GalleryCreate(CreateView):
	model = Gallery
	fields = ['gallery_title', 'gallery_author', 'gallery_date', 'gallery_image', 'gallery_description']

class GalleryUpdate(UpdateView):
	model = Gallery
	fields = ['gallery_title', 'gallery_author', 'gallery_date', 'gallery_image', 'gallery_description']

class GalleryDelete(DeleteView):
	model = Gallery
	success_url = reverse_lazy('gallery')

class ImageCreate(CreateView):
	model = Image
	fields = ['gallery', 'image_title', 'image_image']

class UserFormView(View):
	form_class = UserForm
	template_name = 'kickstv/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})



	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username=username, password=password)

			if user is not None:
			
				if user.is_active:
					login(request, user)
					return redirect('gallery')

		return render(request, self.template_name, {'form': form})