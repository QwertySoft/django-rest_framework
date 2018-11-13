# Importamos los módulos necesarios
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@csrf_exempt # Indicamos que la los endpoints no requieren de un token de csrf
def snippet_list(request): # Definimos una vista que recibe el objeto request
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET': # Implementamos el verbo HTTP GET para obtener todos los snippets
        snippets = Snippet.objects.all() # Recuperamos todos los snippets
        serializer = SnippetSerializer(snippets, many=True) # Creamos el serializador con el QuerySet de todos los snippets
        return JsonResponse(serializer.data, safe=False) # Le devolvemos al cliente un arreglo JSON

    elif request.method == 'POST': # Implementamos el verbo HTTP POST
        data = JSONParser().parse(request) # Obtenemos el JSON payload del request
        serializer = SnippetSerializer(data=data) # Deserializamos los datos
        if serializer.is_valid(): # Corremos las validaciones
            serializer.save() # Persistimos el nuevo snippet
            return JsonResponse(serializer.data, status=201) # Le devolvemos al cliente el snippet creado junto con el HTTP status code 201
        return JsonResponse(serializer.errors, status=400) # Los datos son incorrectos. Le devolvemos al cliente un HTTP status code 400

@csrf_exempt # Indicamos que la los endpoints no requieren de un token de csrf
def snippet_detail(request, pk): # Definimos una vista que recibe el objeto request y la primary key del snippet con el cual vamos a operar
    """
    Retrieve, update or delete a code snippet.
    """
    try: # Decalramos un try/catch por si el snippet no se encuentra en la base de datos
        snippet = Snippet.objects.get(pk=pk) # Intentamos recuperar el snippet con el id pasado como path param
    except Snippet.DoesNotExist: # Definimos el manejador si el snippet no se encuentra en la base de datos
        return HttpResponse(status=404) # Le devolvemos al cliente un HTTP status code 404 porque no encontramos el snippet al que quiere acceder

    if request.method == 'GET': # Implementamos el verbo HTTP GET para un snippet específico
        serializer = SnippetSerializer(snippet) # Creamos el serializador para serializar el snippet
        return JsonResponse(serializer.data) # Le devolvemos al cliente el JSON correspondiente al snippet consultado

    elif request.method == 'PUT': # Implementamos el verbo HTTP PUT para modificar un snippet específico
        data = JSONParser().parse(request) # Obtenemos el JSON payload del request
        serializer = SnippetSerializer(snippet, data=data) # Deserializamos el snippet junto con los datos a modificar
        if serializer.is_valid(): # Corremos las validaciones
            serializer.save() # Actualizamos el snippet
            return JsonResponse(serializer.data) # Le devolvemos al cliente el snippet actualizado
        return JsonResponse(serializer.errors, status=400) # Los datos son incorrectos. Le devolvemos al cliente un HTTP status code 400

    elif request.method == 'DELETE': # Implementamos el verbo HTTP DELETE para eliminar un snippet específico
        snippet.delete() # Eliminamos el snippet de la base de datos
        return HttpResponse(status=204) # Le devolvemos al usuario un HTTP status code 204 indicando que se proceso el requerimiento y no hay datos para devolver