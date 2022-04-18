from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<username>', views.UserView.as_view(), name = 'username'),
]
