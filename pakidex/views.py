from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

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

    # def post(self, request):
    #     form = AuthenticationForm(data = request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(username = username, password = password)
    #         # print(username, password)
    #         if user is not None:
    #             login(request, user = user)
    #
    #             context = {
    #                 'form': form,
    #                 'profile': self.allProfiles,
    #             }
    #
    #             return render(request, 'pakidex/index.html', context)
                # return redirect(f'/{user.username}', username = user.username)


class UserView(View):
    template_name = 'pakidex/userPage.html'
    allProfiles = Profile.objects.all()

    def get_query(self):
        return Card.objects.all()

    def get(self, usrPage, request):
        if 'logout' in request.POST.keys():
            logout(request)
            form = AuthenticationForm()

    def post(self, request, username):
        if 'logout' in request.POST.keys():
            logout(request)
            form = AuthenticationForm()
            return HttpResponseRedirect("http://127.0.0.1:8000/")

        else:
            user = User.objects.get(username=username)
            userDecks = Deck.objects.filter(deck=user)
            for deck in userDecks:
                deck.cards = deck.whoseCard.all()
                for card in deck.cards:
                    print(card.personalName)

            context = {
                # 'form': form,
                'user' : user,
                'profile': self.allProfiles,
                'userDecks' : userDecks,
            }
            print(user.username)
            print(context)
            print(context['userDecks'][0].__dict__)

            return render(request, 'pakidex/userPage.html', context)

class BuildView(View):
    template_name = "pakidex/buildDeck.html"
    allProfiles = Profile.objects.all()

    def get(self, request, username):
        newDeck = Deck()
        newDeck.set(deck=request.user)
        newDeck.save()
        context = {
            'deck' : newDeck,
        }
        context['deck_id'] = newDeck.id
        currUser = User.objects.get(username = username)
        # currUserDecks = Deck.objects.filter(deck = username)
        # self.context['currUser'] = currUser
        # self.context['currUserDecks'] = currUserDecks
        if request.user.username == username:
            self.context['me'] = request.user
            return render(request, 'pakidex/buildDeck.html', self.context)
        else:
            if request.user.is_authenticated:
                self.context['me'] = request.user
                return render(request, 'pakidex/buildDeck.html', self.context)
            else:
                return render(request, 'pakidex/buildDeck.html', self.context)

    def post(self, request, username):
        newDeck = Deck()
        newDeck.set(deck=request.user)
        newDeck.save()
        context = {
            'deck' : newDeck,
        }
        context['deck_id'] = newDeck.id
        newCard = Card(
            personalName = request.POST['pName'],
            species = request.POST['species'],
            type = request.POST['type'],
            level = request.POST['level'],
            health = int(request.POST['level']) * 10,
        )

        newDeck = Deck.objects.filter(id=request.POST['deck_id'])
        newCard.save()
        print("newCard.save()")
        print(newCard)
        newDeck.append(newCard)

        context = {
            'deck' : newDeck,
        }

        return render(request, 'pakidex/buildDeck.html', context)
