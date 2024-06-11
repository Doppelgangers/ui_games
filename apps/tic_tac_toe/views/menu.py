from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View


class Menu(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        context: dict[str, str] = dict(
            title='Меню TitTacToe!',
        )
        return render(request, 'tic_tac_toe/index.html', context=context)
