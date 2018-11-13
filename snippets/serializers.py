from rest_framework import serializers # Importamos el modulo serializers
from snippets.models import Snippet # Importamos el modelo Snippet

class SnippetSerializer(serializers.ModelSerializer): # Definimos un model serializer mediante una clase
    class Meta: # Epecificamos meta-datos
        model = Snippet # Estamos definiciendo un serializador para el modelo Snippet
        fields = ('id', 'title', 'code', 'language') # Idicamos que campos se van a tener en cuenta para la des/serializacion