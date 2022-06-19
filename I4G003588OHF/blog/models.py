from datetime import datetime
from time import timezone
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Post(models.Model):
    # A string of maxlength 200, using Django’s models.CharField
    title = models.CharField(max_length=200)

    # TextField any amount using Django’s TextField
    text = models.TextField()

    # A foreign Key to the current user model. Django's get_user_model function
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # A date-time column, using Django's models.DateTimeField
    created_date = models.DateTimeField()

    # A date-time column, using Django's models.DateTimeField
    published_date = models.DateTimeField()
