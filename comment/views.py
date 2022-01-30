from django.shortcuts import render, redirect
from django.urls import reverse
from comment.models import Comment
from photos.models import Photo
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def createCommentView(request, slug, pk):
    user = request.user 
    photo = Photo.objects.filter(slug=slug, photo_id=pk).first()
    message = request.POST['comment']

    if user is not None and photo is not None and message is not None:
        comment = Comment.objects.create(user=user, message=message, photo=photo)
        comment.save()

    return HttpResponseRedirect(reverse('detail_photo', args=[str(slug), str(pk)]))




@login_required
def deleteCommentView(request, slug, pk):
    user = request.user 
    comment = Comment.objects.filter(slug=slug, comment_id=pk).first()

    if user is not None and comment is not None:
        comment.delete()
        messages.info(request, 'Comment successfully deleted.')

    return redirect('list_photo')





