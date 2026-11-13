# =============================================================================
# admin.py: registra modelos en el panel de administración (/admin/)
# para poder ver, crear, editar y borrar registros desde el navegador.
# =============================================================================

# Módulo del sitio de administración de Django
from django.contrib import admin

# Modelo que se quiere administrar
from .models import Animal

# Registra Animal en el admin con la configuración por defecto
# (se mostrará usando el texto de __str__: "Luna (Gato)")
admin.site.register(Animal)
