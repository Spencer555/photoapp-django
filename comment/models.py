from django.db import models
from django.contrib.auth.models import User 
from photos.models import Photo 
import random 
import string 
from django.utils.text import slugify

# Create your models here.

def generate_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    slug = models.SlugField(blank=True, null=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_name')
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True, related_name='photo_comments')
    message = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.photo.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(generate_slug() + "-1!2@3#0)98*(7&^%$#$@" + self.user.username + '"-1!2@3#0)98*(7&^%$#$@"' + generate_slug())
        super(Comment, self).save(*args, **kwargs)
