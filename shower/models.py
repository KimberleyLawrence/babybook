from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Advice(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User )

    def __str__(self):
        return self.text

    def text_area_rows(self):
        text_length = len(self.text)
        return (text_length / 40) + 3

class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User )

    def __str__(self):
        return self.text


class Gender(models.Model):
    guess = models.CharField(max_length=6)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.guess

class Eye(models.Model):
    guess = models.CharField(max_length=6)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.guess

class Weight(models.Model):
    guess = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    user = models.OneToOneField(User)

    def __str__(self):
        return "%s guessed %s kg" % (self.user, self.guess)


class Date(models.Model):
    guess = models.DateField()
    user = models.OneToOneField(User)

    def __str__(self):
        return '{}'.format(self.guess)


class Time(models.Model):
    guess = models.TimeField()
    user = models.OneToOneField(User)

    def __str__(self):
        return '{}'.format(self.guess)
