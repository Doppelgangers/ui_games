from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from ..forms.room import CreateRoom


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
            form.save()
            return HttpResponse(f"created {request.POST}")

