from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView, View



from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView)


from .models import Autos
from .serializers import AutosSerializer

# Create your views here.


class getUsers(ListAPIView):
    serializer_class = AutosSerializer

    def get_queryset(self):
        return Autos.objects.all()

class detailUser(RetrieveAPIView):
    queryset=Autos.objects.all()
    serializer_class = AutosSerializer
    


class createUser(CreateAPIView):
    serializer_class = AutosSerializer


class updateUser(RetrieveUpdateAPIView):

    serializer_class = AutosSerializer
    queryset = Autos.objects.all()


class deleteUser(DestroyAPIView):
    serializer_class = AutosSerializer
    queryset = Autos.objects.all()

