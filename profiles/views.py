from photos.models import Photo
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from django.contrib.auth.models import User
from django.views.generic import UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse 
from django.http import  HttpResponseRedirect
from user.forms import UserUpdateForm 
from profiles.forms import ProfileUpdateForm




class UpdateProfileView(UserPassesTestMixin ,LoginRequiredMixin ,UpdateView):
    model = Profile 
    template_name = 'profile/update.html'
    context_object_name = 'profiles'
    success_url = 'profiles/profile_list/'
    form_class = ProfileUpdateForm


    def form_valid(self, form):
        form.instance.user == self.request.user
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False


# class DetailProfileView(L, View):
class DetailProfileView(LoginRequiredMixin, DetailView):
    model = Profile 
    template_name = 'profile/detail.html'
    context_object_name = 'profiles'



@login_required
def follow(request, pk, slug):
    profile = Profile.objects.filter(profile_id=pk, slug=slug).first()
    user = request.user 

    if user in profile.followers.all():
        profile.followers.remove(user)

    else:
        profile.followers.add(user)

    
    return HttpResponseRedirect(reverse('profile_detail', args=[str(slug), str(pk)]))


class ListProfileView(ListView):
    model = Profile 
    template_name = 'profile/list.html'
    context_object_name = 'profiles'
    paginate_by = 30





