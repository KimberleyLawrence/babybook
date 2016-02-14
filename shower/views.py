from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from .forms import AdviceForm, MessageForm, GenderForm, WeightForm, DateForm, TimeForm

from .models import Advice, Message, Gender, Weight, Date, Time
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def index(request):
    user_gender_guess = Gender.objects.get(user = request.user)
    return render(request,'index.html',{ 'user_gender_guess': user_gender_guess})

@login_required
def games_gender(request):
    print "gender"
    form = GenderForm()
    return render(request,'games_gender.html',
    {'form': form})

@login_required
def games_gender_guess(request):
    print "gender_guess"
    print request.POST
    form = GenderForm(request.POST)
    if form.is_valid():
        print form.save()
        messages.success(request, 'Your gender guess was sent, select a new game!')
        return HttpResponseRedirect(reverse('index'))
    return render(request,'games_gender.html',
    {'form': form
    })




@login_required
def games_date(request):
    print "date"
    form = DateForm()
    return render(request,'games_date.html',
    {'form': form})

@login_required
def games_date_guess(request):
    print "date_guess"
    print request.POST
    form = DateForm(request.POST)
    print form.save()
    messages.success(request, 'Your date guess was sent, select a new game!')
    return HttpResponseRedirect(reverse('index'))

@login_required
def games_weight(request):
    print "weight"
    form = WeightForm()
    return render(request,'games_weight.html',
    {'form': form})

@login_required
def games_weight_guess(request):
    print "weight_guess"
    print request.POST
    form = WeightForm(request.POST)
    print form.save()
    messages.success(request, 'Your weight guess was sent, select a new game!')
    return HttpResponseRedirect(reverse('index'))

@login_required
def games_time(request):
    print "time"
    form = TimeForm()
    return render(request,'games_time.html',
    {'form': form})

@login_required
def games_time_guess(request):
    print "time_guess"
    print request.POST
    form = TimeForm(request.POST)
    print form.save()
    messages.success(request, 'Your birth time guess was sent, select a new game!')
    return HttpResponseRedirect(reverse('index'))

@login_required
def advice(request):
    print "advice"
    advice_list = Advice.objects.all()
    form = AdviceForm()
    return render(request,'advice.html',
    {'advice_list': advice_list,'form': form
    })

@login_required
def advice_new(request):
    print "advice_new"
    print request.POST
    form = AdviceForm(request.POST)
    if form.is_valid():
        print form.save()
        messages.success(request, 'Your advice was sent, select a new game!')
        return HttpResponseRedirect(reverse('index'))
    return render(request,'advice.html',
    {'form': form
    })

@login_required
def blog(request):
    return render(request,'blog.html',{})

@login_required
def contact(request):
    return render(request,'contact.html',{})

@login_required
def gift(request):
    return render(request,'gift.html',{})

@login_required
def message(request):
    print "message"
    message_list = Message.objects.all()
    form = MessageForm()
    return render(request,'message.html',
    {'message_list': message_list,'form': form
    })

@login_required
def message_new(request):
    print "message_new"
    print request.POST
    form = MessageForm(request.POST)
    print form.save()
    messages.success(request, 'Your advice was sent, select a new game!')
    return HttpResponseRedirect(reverse('index'))
