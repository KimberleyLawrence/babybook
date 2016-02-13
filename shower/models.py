from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Advice(models.Model):
    text = models.TextField()

    user = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.text

class Message(models.Model):
    text = models.TextField()

    user = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.text

class Gender(models.Model):
    guess = models.CharField(max_length=6)

    user = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.guess

class Weight(models.Model):
    guess = models.DecimalField(decimal_places=2, max_digits=4)

    user = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "%s guessed %s kg" % (self.user, self.guess)

class Date(models.Model):
    guess = models.CharField(max_length=100)

    user = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.guess

class Time(models.Model):
    guess = models.CharField(max_length=100)

    user = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.guess
