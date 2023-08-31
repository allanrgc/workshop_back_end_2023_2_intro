from rest_framework import viewsets
from .models import ToDoList, Pessoa
from .serializers import ToDoListSerializer, PessoaSerializer


class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

