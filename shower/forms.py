from django.forms import ModelForm
from .models import *


class AdviceForm(ModelForm):
    class Meta:
        model =  Advice
        fields = ['text', 'user']

class MessageForm(ModelForm):
    class Meta:
        model =  Message
        fields = ['text', 'user']

class GenderForm(ModelForm):
    class Meta:
        model =  Gender
        fields = ['guess', 'user']

class EyeForm(ModelForm):
    class Meta:
        model =  Eye
        fields = ['guess', 'user']

class HairForm(ModelForm):
    class Meta:
        model =  Hair
        fields = ['guess', 'user']

class ParentForm(ModelForm):
    class Meta:
        model =  Parent
        fields = ['guess', 'user']

class WeightForm(ModelForm):
    class Meta:
        model =  Weight
        fields = ['guess', 'user']

class DateForm(ModelForm):
    class Meta:
        model =  Date
        fields = ['guess', 'user']

class TimeForm(ModelForm):
    class Meta:
        model =  Time
        fields = ['guess', 'user']
