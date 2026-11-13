# =============================================================================
# urls.py principal: decide qué código atiende cada URL del proyecto.
# Django revisa urlpatterns en orden y usa la primera ruta que coincida.
# =============================================================================

# Sitio de administración de Django
from django.contrib import admin
# path define una ruta; include delega un prefijo a otro archivo de URLs
from django.urls import include, path
# Vista genérica que solo renderiza una plantilla HTML, sin lógica adicional
from django.views.generic import TemplateView

urlpatterns = [
    # /admin/ -> panel de administración de Django
    path("admin/", admin.site.urls),
    # /api/... -> todas las rutas definidas en animales/urls.py (ej. /api/animales/)
    path("api/", include("animales.urls")),
    # Cliente HTTP local para las seis pruebas
    # "" (la raíz, http://127.0.0.1:8001/) -> muestra templates/cliente.html
    path("", TemplateView.as_view(template_name="cliente.html")),
]
