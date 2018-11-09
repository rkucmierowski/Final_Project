from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from datetime import date


class CustomUser(AbstractUser):
    # office = models.CharField(max_length=64)
    # teryt = models.CharField(max_length=7)
    province = models.CharField(max_length=64, verbose_name='województwo', default="")
    district = models.CharField(max_length=64, verbose_name='powiat', default="")
    municipality = models.CharField(max_length=64, verbose_name='gmina', default="")

    def __str__(self):
        return self.username


class Relic(models.Model):
    name = models.CharField(max_length=128, unique=True)
    time_of_creation = models.CharField(max_length=64, null=True, blank=True)
    date_from = models.DateField(default=date.today, null=True, blank=True)
    date_to = models.DateField(default=date.today, null=True, blank=True)
    place = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    province = models.CharField(max_length=64, null=True, blank=True)
    district = models.CharField(max_length=64, null=True, blank=True)
    municipality = models.CharField(max_length=64, null=True, blank=True)
    forms_of_protection = models.TextField(null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, related_name='relics', blank=True)
    date = models.DateField(default=date.today, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='')
    description = models.CharField(max_length=128, null=True, blank=True)
