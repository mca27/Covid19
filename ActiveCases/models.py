# Create your models here.
from django.db import models
from django.urls import reverse


class IndiaCases(models.Model):
    state_name = models.CharField(max_length=250)
    confirmed_Cases = models.IntegerField()
    active_cases = models.IntegerField()
    recovered = models.IntegerField()
    deaths = models.IntegerField()

    def get_absolute_url(self):
        return reverse('ActiveCases:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.state_name


class Districts(models.Model):
    state = models.ForeignKey(IndiaCases, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=250)
    confirmed_Cases = models.IntegerField()
    active_cases = models.IntegerField()
    recovered = models.IntegerField()
    deaths = models.IntegerField()

    def __str__(self):
        return self.district_name
