from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views import View

from ..forms.room import CreateRoom
from ..models import Room


class GameRoomView(View):
    def get(self, request: HttpRequest, id_room: int) -> HttpResponse:
        room: Room | None = Room.objects.get(pk=id_room)
        return HttpResponse(f"Game {room.name}!")


class CreateRoomView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        context: dict = dict(
            form=CreateRoom(),
            title='Создать комнату',
        )
        return render(request, 'tic_tac_toe/room/room.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form: CreateRoom = CreateRoom(request.POST)
        if form.is_valid():
            room: Room = form.save()
            return HttpResponseRedirect(reverse('ttt_game', args=(room.pk,)))
