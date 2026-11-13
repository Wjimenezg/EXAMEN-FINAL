from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet

# Crea el router
router = DefaultRouter()

# Registra el recurso
router.register("animales", AnimalViewSet, basename="animal")

# Django lee esta variable para conocer las rutas de la app
urlpatterns = router.urls
