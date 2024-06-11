from django.urls import path
from .views import menu, room

urlpatterns = [
    path('', menu.Menu.as_view(), name='ttt_menu'),
    path('create_room/', room.CreateRoomView.as_view(), name='ttt_create_room'),
    path('game/<int:id_room>/', room.GameRoomView.as_view(), name='ttt_game'),
]
