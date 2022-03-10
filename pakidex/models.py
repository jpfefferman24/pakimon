from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE, primary_key = True)
    verified = models.BooleanField(default = False)

class Deck(models.Model):
    deck = models.OneToOneField(deck, on_delete=models.CASCADE, primary_key = True)
    verified = models.BooleanField(default = False)

class Card(models.Model):
    pakiName = models.CharField(max_length = 280)
    whoseDeck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    moves = []

class Move(models.Model):
    move = models.ForeignKey(
        Card,
        on_delete = models.CASCADE,
        null = True,
    )

class Pakimon(models.Model):
    paki = models.ForeignKey(
        Card,
        on_delete = models.CASCADE
        null = True,
    )
