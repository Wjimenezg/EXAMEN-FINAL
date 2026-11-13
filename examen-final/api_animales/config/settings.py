# =============================================================================
# settings.py: configuración central del proyecto Django.
# Django lee este archivo al arrancar (manage.py le indica que use
# "config.settings" mediante la variable DJANGO_SETTINGS_MODULE).
# =============================================================================

# Path permite trabajar con rutas de archivos de forma independiente del sistema operativo
from pathlib import Path

# BASE_DIR apunta a la carpeta raíz del proyecto (api_animales/).
# __file__ es este archivo; .parent sube a config/ y otro .parent sube a api_animales/
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave usada por Django para firmar cookies, sesiones y tokens CSRF.
# En un proyecto real debe ser secreta y no subirse a un repositorio.
SECRET_KEY = "dev-solo-para-pruebas-cambiar-en-produccion"

# DEBUG=True muestra errores detallados en el navegador. Solo para desarrollo.
DEBUG = True

# Lista de nombres de host desde los que Django acepta peticiones.
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Aplicaciones instaladas: Django solo carga modelos, admin, migraciones, etc.
# de las apps que aparecen en esta lista.
INSTALLED_APPS = [
    "django.contrib.admin",          # Panel de administración en /admin/
    "django.contrib.auth",           # Sistema de usuarios y permisos
    "django.contrib.contenttypes",   # Registro de los modelos del proyecto (lo usa auth/admin)
    "django.contrib.sessions",       # Manejo de sesiones (necesario para el admin)
    "django.contrib.messages",       # Mensajes temporales (los que muestra el admin)
    "django.contrib.staticfiles",    # Sirve archivos estáticos (CSS/JS) en desarrollo
    "rest_framework",                # Django REST Framework: herramientas para construir la API
    "corsheaders",                   # Permite peticiones desde otros orígenes (ej. React en :5173)
    "animales",                      # Nuestra app con el modelo, serializer y vistas de animales
]

# Middleware: capas que procesan cada petición (de arriba hacia abajo)
# y cada respuesta (de abajo hacia arriba). El orden importa.
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # debe ir lo más arriba posible
    "django.middleware.security.SecurityMiddleware",            # Cabeceras de seguridad básicas
    "django.contrib.sessions.middleware.SessionMiddleware",     # Carga la sesión del usuario
    "django.middleware.common.CommonMiddleware",                # Ajustes comunes (ej. barra final en URLs)
    "django.middleware.csrf.CsrfViewMiddleware",                # Protección CSRF para formularios
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Añade request.user
    "django.contrib.messages.middleware.MessageMiddleware",     # Habilita el sistema de mensajes
    "django.middleware.clickjacking.XFrameOptionsMiddleware",   # Evita que la página se cargue en un iframe ajeno
]

# Módulo donde está la lista principal de URLs (config/urls.py)
ROOT_URLCONF = "config.urls"

# Configuración del motor de plantillas (HTML)
TEMPLATES = [
    {
        # Usa el motor de plantillas propio de Django
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Carpeta extra donde buscar plantillas: api_animales/templates/ (ahí está cliente.html)
        "DIRS": [BASE_DIR / "templates"],
        # También busca en la carpeta templates/ de cada app instalada (lo usa el admin)
        "APP_DIRS": True,
        "OPTIONS": {
            # Variables que se agregan automáticamente al contexto de cada plantilla
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Punto de entrada WSGI que usa el servidor para ejecutar la aplicación
WSGI_APPLICATION = "config.wsgi.application"

# ---- Base de datos MySQL/MariaDB (XAMPP) ----
DATABASES = {
    "default": {
        # Backend de MySQL. Funciona gracias a PyMySQL (ver config/__init__.py)
        "ENGINE": "django.db.backends.mysql",
        # Nombre de la base de datos (debe existir antes de correr migrate)
        "NAME": "api_animales",
        # Usuario de MySQL. En XAMPP, root viene sin contraseña
        "USER": "root",
        # Contraseña vacía, como trae XAMPP por defecto
        "PASSWORD": "",
        # Se usa la IP en lugar de "localhost" para forzar conexión TCP
        "HOST": "127.0.0.1",
        # Puerto donde escucha el MariaDB de XAMPP en ESTA computadora.
        # Ojo: el 3306 lo ocupa otro servidor MySQL (no el de XAMPP) cuyo root
        # sí tiene contraseña; conectarse ahí provoca el error 1045 "Access denied".
        "PORT": "3307",
        # utf8mb4 permite guardar cualquier carácter (tildes, ñ, emojis)
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

# Idioma de la interfaz de Django (mensajes del admin, errores de validación, etc.)
LANGUAGE_CODE = "es"
# Zona horaria usada para mostrar fechas
TIME_ZONE = "America/Guatemala"
# Activa la traducción de textos de Django
USE_I18N = True
# Guarda las fechas en UTC en la base de datos y las convierte según TIME_ZONE
USE_TZ = True

# URL base para archivos estáticos (CSS, JS, imágenes)
STATIC_URL = "static/"
# Tipo de llave primaria automática para los modelos (entero de 64 bits)
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configuración global de Django REST Framework.
# La API responde solo en JSON
REST_FRAMEWORK = {
    # Las respuestas se devuelven solo como JSON (sin la página navegable de DRF)
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    # Solo se aceptan cuerpos de petición en formato JSON
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
    # Sin autenticación: así tampoco se exige token CSRF en POST/PUT/DELETE
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    # Cualquiera puede usar la API (adecuado solo para pruebas/examen)
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
}

# Permite que una app de React (Vite o CRA) consuma la API.
# El navegador bloquea peticiones entre orígenes distintos (CORS) salvo que
# el servidor los autorice; aquí se autorizan los puertos típicos de React.
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",   # Vite
    "http://127.0.0.1:5173",   # Vite (por IP)
    "http://localhost:3000",   # Create React App
    "http://127.0.0.1:3000",   # Create React App (por IP)
]
