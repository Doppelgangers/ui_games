from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

class Menu(View):

    def get(self, request) -> HttpResponse:
        return render(request, 'tic_tac_toe/index.html')
