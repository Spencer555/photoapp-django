from django.db import models
from django.contrib.auth.models import User 
import random 
import string 
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from PIL import Image

# Create your models here.

def generate_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/profile/images", default='media/profile/images/default.jpg')
    slug = models.SlugField(blank=True, null=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, blank=True, related_name='profile_followers')
    about = models.TextField()


    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(generate_slug() + "-1!2@3#0)98*(7&^%$#$@" + self.user.username + '"-1!2@3#0)98*(7&^%$#$@"' + generate_slug())
        super(Profile, self).save(*args, **kwargs)






@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
