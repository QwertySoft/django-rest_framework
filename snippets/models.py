from django.db import models # Importamos el modulo models de Django

# Declaramos un arreglo de opciones
LANGUAGE_CHOICES = [
    ('PYTHON', 'Python'),
    ('JAVA', 'Java'),
    ('PHP', 'PHP'),
]

class Snippet(models.Model): # Declaramos nuestro modelo Snippet
    created = models.DateTimeField(auto_now_add=True) # Declaramos el campo created
    title = models.CharField(max_length=100, blank=True, default='') # Declaramos el campo title
    code = models.TextField() # Declaramos el campo code
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100) # Declaramos el campo language

    class Meta: # Declaramos los metadatos
        ordering = ('-created',) # Indicamos que el orden por defecto de los snippets es por fecha de creacion descendiente