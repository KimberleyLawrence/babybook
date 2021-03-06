from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Advice(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User )

    def __str__(self):
        return "%s wrote  %s" % (self.user, self.text)

    def text_area_rows(self):
        text_length = len(self.text)
        return (text_length / 40) + 3

@python_2_unicode_compatible
class Message(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User )

    def __str__(self):
        return "%s wrote  %s" % (self.user, self.text)


class Gender(models.Model):
    guess = models.CharField(max_length=6)
    user = models.OneToOneField(User)

    def __str__(self):
        return "%s guessed %s" % (self.user, self.guess)

class Eye(models.Model):
    guess = models.CharField(max_length=6)
    user = models.OneToOneField(User)

    def __str__(self):
        return "%s guessed %s" % (self.user, self.guess)

class Hair(models.Model):
    guess = models.CharField(max_length=6)
    user = models.OneToOneField(User)

    def __str__(self):
        return "%s guessed %s" % (self.user, self.guess)

class Parent(models.Model):
    guess = models.CharField(max_length=7)
    user = models.OneToOneField(User)

    def __str__(self):
        return "%s guessed %s" % (self.user, self.guess)

class Weight(models.Model):
    guess = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    user = models.OneToOneField(User)

    def __str__(self):
        return "%s guessed %s kg" % (self.user, self.guess)


class Date(models.Model):
    guess = models.DateField()
    user = models.OneToOneField(User)

    def __str__(self):
        return "%s guessed %s" % (self.user, self.guess)


class Time(models.Model):
    guess = models.TimeField()
    user = models.OneToOneField(User)

    def __str__(self):
        return "%s guessed %s" % (self.user, self.guess)
