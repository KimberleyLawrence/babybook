from django.contrib import admin
from .models import Advice, Message, Gender, Weight, Date, Time

admin.site.register(Advice)
admin.site.register(Message)
admin.site.register(Gender)
admin.site.register(Weight)
admin.site.register(Date)
admin.site.register(Time)
