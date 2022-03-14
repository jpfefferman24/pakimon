from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    verified = models.BooleanField(default = False)

class Deck(models.Model):
    deck = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    verified = models.BooleanField(default = False)

class Card(models.Model):
    personalName = models.CharField(max_length = 280)
    whoseDeck = models.ForeignKey(Deck, on_delete=models.CASCADE)

class Move(models.Model):
    whichCard = models.ForeignKey(
        Card,
        on_delete = models.CASCADE,
        null = True,
    )
    moveName = models.CharField(max_length = 280)
    moveNum = models.IntegerField(default = -1)

    def __str__(self):
        moveStr = "Move Name: " + moveName + ", Move Number: " + moveNum
        return moveStr

class Pakimon(models.Model):
    whichCard = models.ForeignKey(
        Card,
        on_delete = models.CASCADE,
        null = True,
    )
    pakiName = models.CharField(max_length = 280)

    def __str__(self):
        pakiStr = "Pakimon Name: " + pakiName
        return pakiStr
