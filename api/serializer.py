# Este serializador que vamos a crear nos va a poder convertir el modelo Programmer en una lista de elementos de formato JSON 
# para serializarlo, tanto de ida como de vuelta para enviar como para recibir sin hacerlo nosotros manualmente.

from rest_framework import serializers
from .models import Programmer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        #fields = ('fullname', 'nickname', )
        fields = '__all__' # Para indicar que se serializen todos los campos de nuestro modelo + el id.
        
    

 