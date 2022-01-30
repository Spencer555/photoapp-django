from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from photos.models import Photo
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from comment.forms import CommentForm
from django.db.models import Q
from photos.forms import PhotoForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# photos



class CreatePhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photos/create.html'
    context_object_name = 'photos'
    success_url = '/'
    form_class = PhotoForm



    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class DetailPhotoView(DetailView):
    model = Photo 
    template_name = 'photos/detail.html'
    context_object_name = 'photos'


class ListPhotoView(ListView):
    model = Photo
    template_name = 'photos/list.html'
    context_object_name ='photos'
    paginate_by = 12
    ordering = ['-uploaded']



class DeletePhotoView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photos/delete.html'
    context_object_name = 'photos'

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.user:
            return True 
        return False








class UpdatePhotoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    template_name = 'photos/update.html'
    context_object_name = 'photos'
    success_url = '/'
    form_class = PhotoForm



    def form_valid(self, form):
        form.instance.user == self.request.user
        return super().form_valid(form)

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.user:
            return True
        return False


@login_required
def likePhoto(request, pk, slug):
    photo = Photo.objects.filter(photo_id=pk, slug=slug).first()
    user = request.user 

    if user in photo.likes.all():
        photo.likes.remove(user)
        photo.dislikes.remove(user)

    elif user in photo.dislikes.all():
        photo.dislikes.remove(user)
        photo.likes.add(user)

    else:
        photo.likes.add(user)

    
    return HttpResponseRedirect(reverse('detail_photo', args=[str(slug), str(pk)]))
    



    
@login_required
def dislikePhoto(request, pk, slug):
    photo = Photo.objects.filter(photo_id=pk, slug=slug).first()
    user = request.user 

    if user in photo.dislikes.all():
        photo.dislikes.remove(user)
        photo.likes.remove(user)

    elif user in photo.likes.all():
        photo.likes.remove(user)
        photo.dislikes.add(user)

    else:
        photo.dislikes.add(user)

    
    return HttpResponseRedirect(reverse('detail_photo', args=[str(slug), str(pk)]))
    



    

class SearchView(View):
        
    def post(self, request):
        query = request.data.get('q')
        photo = Photo.objects.filter(Q(name__icontains=query))
        
        context = {
            'photo': photo,
            'query': query
            
            }

        return render(request, 'photos/search.html', context)
     
