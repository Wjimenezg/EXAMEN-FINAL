# =============================================================================
# views.py: las vistas reciben la petición HTTP y devuelven la respuesta.
# Con un ModelViewSet, DRF ya trae implementado todo el CRUD; solo hay que
# decirle QUÉ datos usar (queryset) y CÓMO convertirlos (serializer_class).
# =============================================================================

# viewsets contiene ModelViewSet, que agrupa las 5 operaciones del CRUD
from rest_framework import viewsets

# Modelo con los datos y serializer que valida/convierte a JSON
from .models import Animal
from .serializers import AnimalSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    GET    /api/animales/        -> listar      (200)
    POST   /api/animales/        -> crear       (201, o 400 si hay datos inválidos)
    GET    /api/animales/<id>/   -> consultar   (200, o 404)
    PUT    /api/animales/<id>/   -> actualizar  (200, o 400)
    DELETE /api/animales/<id>/   -> eliminar    (204)
    """

    # Registros sobre los que trabaja la vista: todos los animales de la tabla
    queryset = Animal.objects.all()
    # Serializer que se usa para validar la entrada y dar formato JSON a la salida
    serializer_class = AnimalSerializer
