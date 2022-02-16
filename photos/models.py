from django.db import models
from django.contrib.auth.models import User 
import random 
import string
from django.utils.text import slugify
from PIL import Image
# Create your models here.

def generate_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))



class Photo(models.Model):
    slug = models.SlugField(blank=True, null=True, editable=False)
    photo_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photo_owner')
    likes = models.ManyToManyField(User, blank=True, related_name='photo_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='photo_dislikes')
    name = models.CharField(max_length=150)
    image = models.ImageField()
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user.username} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(generate_slug() + "-1!2@3#0)98*(7&^%$#$@" + self.user.username + '"-1!2@3#0)98*(7&^%$#$@"' + generate_slug())

        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        image.resize((300,300))
        image.save(self.image.path, quality=10, optimize=True)
