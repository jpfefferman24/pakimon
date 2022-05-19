from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<username>', views.UserView.as_view(), name = 'username'),
    path('<username>/build', views.BuildDeckView.as_view(), name="buildDeck"),
    path('<username>/build/card', views.BuildCardView.as_view(), name="buildCard"),
]
