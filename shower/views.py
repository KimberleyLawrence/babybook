from django.http import HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AdviceForm, MessageForm, GenderForm, WeightForm, DateForm, TimeForm
from .models import Advice, Message, Gender, Weight, Date, Time

##-----------------------------INDEX-----------------------------
@login_required
def index(request):
    user_gender_guess = Gender.objects.filter(user = request.user).first()
    user_weight_guess = Weight.objects.filter(user = request.user).first()
    user_date_guess = Date.objects.filter(user = request.user).first()
    user_time_guess = Time.objects.filter(user = request.user).first()

    return render(request,'index.html',{
        'user_gender_guess': user_gender_guess,
        'user_weight_guess': user_weight_guess,
        'user_date_guess': user_date_guess,
        'user_time_guess': user_time_guess
    })

##---------------------------LOGIN------------------------------------
@login_required
def games_gender(request):
    print "gender"
    form = GenderForm()
    return render(
        request,
        'games_gender.html',
        {
        'form': form,
        ## CHANGE ME
        'title': 'Guess the Gender',
        'description': 'Click on the gender you think Bubs will be,  once you click the gender, your guess will be sent.',
        'icons': ['fa-venus', 'fa-mars'],
        'color': 'green'
        ## / CHANGE ME
        }
    )

##-------------------------GENDER-----------------------------------
@login_required
def games_gender_guess(request):
    print "gender_guess"
    print request.POST
    gender = Gender.objects.filter(user = request.user).first()
    form = GenderForm(request.POST, instance = gender)

    if form.is_valid():
        print form.save()
        messages.success(request, 'Your gender guess was sent, select a new game!')
        return HttpResponseRedirect(reverse('index'))

    return render(
        request,
        'games_gender.html',
        {
            'form': form,
            ## CHANGE ME
            'title': 'Guess the Gender',
            'description': 'Click on the gender you think Bubs will be,  once you click the gender, your guess will be sent.',
            'icons': ['fa-smile-o'],
            'color': 'purple'
            ## / CHANGE ME
        }
    )

##----------------------------------DATE--------------------------------------
@login_required
def games_date(request):
    print "date"
    form = DateForm()
    return render(
        request,
        'games_date.html',
        {
            'form': form,
            ## CHANGE ME
            'title': 'Guess the Date Baby Maddock will be Born',
            'description': 'Select the date you think baby Maddock will enter the world',
            'icons': ['fa-calendar'],
            'color': 'purple'
            ## / CHANGE ME
        }
    )


@login_required
def games_date_guess(request):
    print "date_guess"
    print request.POST
    date = Date.objects.filter(user = request.user).first()
    form = DateForm(request.POST, instance = date)
    if form.is_valid():
        print form.save()
        messages.success(request, 'Your birth date guess was sent, select a new game!')
        return HttpResponseRedirect(reverse('index'))
    return render(
        request,
        'games_date.html',
        {
            'form': form,
            ## CHANGE ME
            'title': 'Guess the Date Baby Maddock will be Born',
            'description': 'Select the date you think baby Maddock will enter the world',
            'icons': ['fa-calendar'],
            'color': 'purple'
            ## / CHANGE ME
        }
    )
##-----------------------------------WEIGHT--------------------------------------
@login_required
def games_weight(request):
    print "weight"
    weight = Weight.objects.filter(user = request.user).first()
    form = WeightForm(instance = weight)
    return render(
        request,
        'games_weight.html',
        {
            'title': 'Guess the Weight',
            'description': 'Type your guess of bubs birth weight in either Kilograms (eg. 3.34) or in Pounds and Ounces',
            'icons': ['fa-balance-scale'],
            'form': form,
            'color': 'green'
        }
    )


@login_required
def games_weight_guess(request):
    print "weight_guess"
    print request.POST
    weight = Weight.objects.filter(user = request.user).first()
    form = WeightForm(request.POST, instance = weight)
    print form.save()
    messages.success(request, 'Your weight guess was sent, select a new game!')
    return HttpResponseRedirect(reverse('index'))

##--------------------------------TIME-------------------------------------------
@login_required
def games_time(request):
    print "time"
    time = Time.objects.filter(user = request.user).first()
    form = TimeForm(instance = time)
    return render(
        request,
        'games_time.html',
        {
            'form': form,
            ## CHANGE ME
            'title': 'Guess the Time Baby Maddock will be Born',
            'description': 'Use the arrows to guess what time Baby Maddock with come into the world.',
            'icons': ['fa-clock-o'],
            'color': 'green'
            ## / CHANGE ME
        }
    )


@login_required
def games_time_guess(request):
    print "time_guess"
    print request.POST
    time = Time.objects.filter(user = request.user).first()
    form = TimeForm(request.POST, instance = time)
    print form.save()
    messages.success(request, 'Your birth time guess was sent, select a new game!')
    return HttpResponseRedirect(reverse('index'))

##--------------------------ADVICE---------------------------------------------
@login_required
def advice(request):
    print "advice"
    advice_list = Advice.objects.all()
    form = AdviceForm()
    return render(
        request,
        'advice.html',
        {
            'advice_list': advice_list,
            'form': form,
            ## CHANGE ME
            'title': 'Advice for the Parents to Be',
            'description': 'Send a message of positive advice, funny pregnancy/parenting stories, and things the parents to be have to look forward to.',
            'icons': ['fa-comment-o'],
            'color': 'blue '
            ## / CHANGE ME
        }
    )
@login_required
def advice_single(request, advice_id):
    print "advice_single"
    advice = Advice.objects.get(id=advice_id)

    return render(
        request,
        'advice.html',
        {
            'advice': advice,
            ## CHANGE ME
            'title': 'Advice for the Parents to Be',
            'description': 'Send a message of positive advice, funny pregnancy/parenting stories, and things the parents to be have to look forward to.',
            'icons': ['fa-comment-o'],
            'color': 'blue '
            ## / CHANGE ME
        }
    )


@login_required
def advice_new(request):
    print "advice_new"
    print request.POST
    form = AdviceForm(request.POST)

    if form.is_valid():
        print form.save()
        messages.success(request, 'Your advice was sent, select a new game!')
        return HttpResponseRedirect(reverse('index'))

    return render(
        request,
        'advice.html',
        {
            'form': form,
            ## CHANGE ME
            'title': 'Leave a message for Baby Maddock',
            'description': 'It could be a message of love, a poem, just something sweet that Leigh and Krystal can keep and read to Bubs as they grow up.',
            'icons': ['fa-smile-o'],
            'color': 'purple'
            ## / CHANGE ME
        }
    )

##-----------------------------------BLOG----------------------------------------
@login_required
def blog(request):
    return render(request,'blog.html',{
    'title': "Krystal and Leigh's Baby Update Blog",
    'description': 'Tune in here to get updates of Baby Maddock As Leigh and Krystal prepare to become Mum and Dad.',
    'icons': ['fa-heart-o'],
    'color': 'purple'
    })

##---------------------------------CONTACT-----------------------------------------
@login_required
def contact(request):
    return render(request,'contact.html',{
    'title': "Contact",
    'description': 'If you would like to contact the parents to be, or if you have any other questions.',
    'icons': ['fa-envelope-o'],
    'color': 'purple'
    })

##-------------------------------GIFT--------------------------------------------
@login_required
def gift(request):
    return render(request,'gift.html',{
        'title': 'Gift Registry',
        'description': 'If you would like to buy a gift for Baby Maddock. Here is a registry the parents to be have created with things they will need for their new bundle of joy.',
        'icons': ['fa-gift'],
        'color': 'blue'
    })

##----------------------------MESSAGE--------------------------------------------
@login_required
def message(request):
    print "message"
    message_list = Message.objects.all()
    form = MessageForm()
    return render(
        request,
        'message.html',
        {
            'message_list': message_list,
            'form': form,
            'title': 'Leave a message for Baby Maddock',
            'description': 'It could be a message of love, a poem, just something sweet that Leigh and Krystal can keep and read to Bubs as they grow up.',
            'icons': ['fa-smile-o'],
            'color': 'purple'
        }
    )

@login_required
def message_single(request, message_id):
    print "message_single"
    message = Message.objects.get(id=message_id)

    return render(
        request,
        'message.html',
        {
            'message': message,
            'title': 'Leave a message for Baby Maddock',
            'description': 'It could be a message of love, a poem, just something sweet that Leigh and Krystal can keep and read to Bubs as they grow up.',
            'icons': ['fa-smile-o'],
            'color': 'purple'
        }
    )

@login_required
def message_new(request):
    print "message_new"
    print request.POST
    form = MessageForm(request.POST)
    if form.is_valid():
        print form.save()
        messages.success(request, 'Your message was sent, select a new game!')
        return HttpResponseRedirect(reverse('index'))
    return render(
        request,
        'message.html',
        {
            'form': form,
            'title': 'Leave a message for Baby Maddock',
            'description': 'It could be a message of love, a poem, just something sweet that Leigh and Krystal can keep and read to Bubs as they grow up.',
            'icons': ['fa-smile-o'],
            'color': 'purple'
        }
    )
