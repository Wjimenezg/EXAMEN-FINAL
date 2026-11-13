# urls.py de la app animales: conecta el ViewSet con sus URLs.
# Este archivo se incluye desde config/urls.py bajo el prefijo "api/".


#genera automáticamente las rutas de un ViewSet
from rest_framework.routers import DefaultRouter

# ViewSet con las operaciones CRUD de animales
from .views import AnimalViewSet

# Se crea el router que construirá la lista de URLs
router = DefaultRouter()
# Registra el ViewSet bajo el prefijo "animales". Esto genera:
#   animales/        -> list (GET) y create (POST)
#   animales/<pk>/   -> retrieve (GET), update (PUT), partial_update (PATCH), destroy (DELETE)
# basename es el nombre base de las rutas ("animal-list", "animal-detail")
router.register("animales", AnimalViewSet, basename="animal")

# Django busca la variable urlpatterns; aquí se usan las rutas generadas por el router
urlpatterns = router.urls
