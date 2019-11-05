from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  card = models.BigIntegerField(blank=False)
  phone = models.CharField(max_length=11, blank=True)
