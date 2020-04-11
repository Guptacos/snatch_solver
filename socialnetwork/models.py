from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Comment(models.Model):
    # Note that we can't delete Users or Posts, so on_delete not needed
    created_by      = models.ForeignKey(
                            User,
                            on_delete=models.DO_NOTHING
                      )
    creation_time   = models.DateTimeField()
    text            = models.CharField(
                            blank=True,
                            max_length=200
                      )

    def __str__(self):
        return 'Comment(text=' + self.text + ')'

class Post(models.Model):
    # Note that we can't delete Users, so on_delete not needed
    created_by      = models.ForeignKey(
                            User,
                            on_delete=models.DO_NOTHING
                      )
    creation_time   = models.DateTimeField()
    post_input_text = models.CharField(
                            blank=True,
                            max_length=200,
                      )
    comments        = models.ManyToManyField(
                            Comment,
                            blank=True
                    )

    def __str__(self):
        return 'Post(text=' + self.text + ')'

# Method to rename user-submitted profile pictures
def profile_pic_path(instance, filepath):
    # Use same file extension
    ext = '.' + filepath.split('.')[-1] if len(filepath.split('.')) > 1 else ''
    return '{0}_profile{1}'.format(instance.user.username, ext)

# This class acts as an extension of the Django User class. While User is used
# for authentication, this class is used to store auxilliary user information
class Profile(models.Model):
    user            = models.OneToOneField(
                            settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,
                            editable=False,
                            unique=True
                      )
    username        = models.CharField(
                            max_length=50
                      )
    profile_picture = models.ImageField(
                            upload_to=profile_pic_path,
                            default='blank_profile_picture.png'
                      )
    bio_input_text  = models.TextField(
                            max_length=500,
                            blank=True
                      )
    following       = models.ManyToManyField(
                            "self",
                            symmetrical=False
                      )