from django.contrib import admin

from .models import Profile, Deck, Card, Move
# Register your models here.

admin.site.register(Profile)
admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(Move)
