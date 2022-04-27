from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    verified = models.BooleanField(default = False)

class Card(models.Model):
    Grass = 'gr'
    Water = 'h20'
    Fire = 'fr'
    Ice = 'ic'
    Flying = 'fy'
    Rock = 'ro'
    typeList = [
        (Grass, 'Grass'),
        (Water, 'Water'),
        (Fire, 'Fire'),
        (Ice, 'Ice'),
        (Flying, 'Flying'),
        (Rock, 'Rock'),
    ]
    Bulbasaur = 'bulb'
    Squirtle = 'sqrt'
    personalName = models.CharField(max_length = 280)
    species = models.CharField(max_length = 280)
    type = models.CharField(max_length = 12, choices = typeList, default = Grass,)
    level = models.IntegerField(default = 1)
    health = models.IntegerField(default = 1)

class Deck(models.Model):
    deck = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    verified = models.BooleanField(default = False)
    whoseCard = models.ManyToManyField(Card)

class Move(models.Model):
    whichCard = models.ForeignKey(
        Card,
        on_delete = models.CASCADE,
        null = True,
    )
    moveName = models.CharField(max_length = 280)
    moveNum = models.IntegerField(default = -1)

    def __str__(self):
        moveStr = "Move Name: " + self.moveName + ", Move Number: " + str(self.moveNum)
        return moveStr

class Pakimon(models.Model):
    whichCard = models.ForeignKey(
        Card,
        on_delete = models.CASCADE,
        null = True,
    )
    pakiName = models.CharField(max_length = 280)

    def __str__(self):
        pakiStr = "Pakimon Name: " + self.pakiName
        return pakiStr
