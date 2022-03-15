from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Profile, Deck, Card, Move, Pakimon

# Create your views here.
class IndexView(View):
    allProfiles = Profile.objects.all()

    def get(self, request):
        context = {
            'profile': self.allProfiles,
        }

        return render(request, 'pakidex/index.html', context)

class DeckView(View):
    model = Card
    template_name = 'pakidex/deck.html'

    def get_query(self):
        return Card.objects.all()
