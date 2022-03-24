from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Deck, Card, Move, Pakimon

# Create your views here.
class IndexView(View):
    allProfiles = Profile.objects.all()

    def get(self, request):

        form = AuthenticationForm()

        context = {
            'form': form,
            'profile': self.allProfiles,
            'user': request.user,
        }

        return render(request, 'pakidex/index.html', context)

    def post(self, request):
        if 'logout' in request.POST.keys():
            logout(request)
            form = AuthenticationForm()

        else:
            form = AuthenticationForm(data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                passsword = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                print(username, password)
                if user is not None:
                    login(request, user = user)

        context = {
            'form': form,
            'profile': self.allProfiles,
        }

        return render(request, 'pakidex/index.html', context)

class DeckView(View):
    model = Card
    template_name = 'pakidex/deck.html'

    def get_query(self):
        return Card.objects.all()
