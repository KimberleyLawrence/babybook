from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'games/gender/guess/', views.games_gender_guess, name='games_gender_guess'),
    url(r'games/gender/', views.games_gender, name='games_gender'),

    url(r'games/date/guess', views.games_date_guess, name='games_date_guess'),
    url(r'games/date', views.games_date, name='games_date'),


    url(r'games/weight/guess', views.games_weight_guess, name='games_weight_guess'),
    url(r'games/weight', views.games_weight, name='games_weight'),

    url(r'games/time/guess', views.games_time_guess, name='games_time_guess'),
    url(r'games/time', views.games_time, name='games_time'),

    url(r'advice/(?P<advice_id>[0-9]+)', views.advice_single, name='advice_single'),
    url(r'advice/new', views.advice_new, name='advice_new'),
    url(r'advice/', views.advice, name='advice'),

    url(r'blog', views.blog, name='blog'),

    url(r'contact', views.contact, name='contact'),

    url(r'gift', views.gift, name='gift'),

    url(r'message/(?P<message_id>[0-9]+)', views.message_single, name='message_single'),
    url(r'message/new', views.message_new, name='message_new'),
    url(r'message/', views.message, name='message'),

    url(r'games/eye/guess/', views.games_eye_guess, name='games_eye_guess'),
    url(r'games/eye/', views.games_eye, name='games_eye'),

        ]
