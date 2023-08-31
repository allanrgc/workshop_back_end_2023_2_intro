from rest_framework import serializers
from .models import ToDoList, Pessoa

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'