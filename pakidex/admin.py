from django.contrib import admin

from .models import Profile, Deck, Card, Move, Pakimon
# Register your models here.

admin.site.register(Profile)
admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(Move)
admin.site.register(Pakimon)
