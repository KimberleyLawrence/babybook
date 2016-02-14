from django.forms import ModelForm
from .models import Advice, Message, Gender, Weight, Date, Time


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
