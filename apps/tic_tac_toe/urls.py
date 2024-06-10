from django.urls import path
from . import views

urlpatterns = [
    path('', views.TickTacToeMenu.as_view(), name='tic_tac_toe_menu'),
]
