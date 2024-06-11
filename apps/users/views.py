from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'core/index.html')
