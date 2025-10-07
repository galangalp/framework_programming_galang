from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Warga

class WargaListView(ListView):
    model = Warga
class WargaDetailListView(DetailView):
    model = Warga