from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            # print(username, password)
            if user is not None:
                login(request, user = user)

                context = {
                    'form': form,
                    'profile': self.allProfiles,
                }

                # return render(request, 'pakidex/userPage.html', context)
                # return redirect(f'/{user.username}', username = user.username)

                userDecks = Deck.objects.filter(deck=user)

                context = {
                    'form': form,
                    'profile': self.allProfiles,
                    'deck' : userDecks,
                }
                print(context)

                return render(request, 'pakidex/userPage.html', context)

class UserView(View):
    template_name = 'pakidex/userPage.html'

    def get_query(self):
        return Card.objects.all()

    def get(self, usrPage, request):
        if 'logout' in request.POST.keys():
            logout(request)
            form = AuthenticationForm()
