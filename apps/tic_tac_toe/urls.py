from django.urls import path
from .views import menu

urlpatterns = [
    path('', menu.Menu.as_view(), name='tic_tac_toe_menu'),
]
