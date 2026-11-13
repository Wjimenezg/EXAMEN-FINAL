# =============================================================================
# serializers.py: el serializer es el "traductor" entre JSON y el modelo.
#   - Salida: convierte objetos Animal a diccionarios/JSON para la respuesta.
#   - Entrada: recibe el JSON de un POST/PUT, lo VALIDA y, si es correcto,
#     crea o actualiza el registro en la base de datos.
#
# ¿De dónde salen los errores 400?
#   La vista (ModelViewSet) llama a serializer.is_valid(raise_exception=True).
#   Si algún campo falla, el serializer junta los errores en un diccionario
#   {"campo": ["mensaje"]} y lanza ValidationError. DRF captura esa excepción
#   y responde automáticamente con 400 Bad Request y ese diccionario como JSON.
#   En ese caso NO se guarda nada en la base de datos.
#
# Orden de validación de cada campo:
#   1. ¿Viene el campo? Si no -> error "required" (solo en POST y PUT; PATCH no lo exige).
#   2. ¿Tiene un valor válido para su tipo? Si está vacío -> "blank";
#      si no es número -> "invalid"; si es muy largo -> "max_length".
#   3. Validaciones personalizadas validate_<campo> (ej. validate_edad).
# =============================================================================

# serializers contiene ModelSerializer, los tipos de campo y ValidationError
from rest_framework import serializers

# Modelo que este serializer va a leer y escribir
from .models import Animal


# ModelSerializer genera los campos automáticamente a partir del modelo,
# pero aquí se declaran a mano para personalizar los mensajes de error.
class AnimalSerializer(serializers.ModelSerializer):
    # Campos obligatorios con mensajes de error en español
    # Por defecto todo campo declarado así es required=True (obligatorio)
    nombre = serializers.CharField(
        max_length=100,  # Mismo límite que en el modelo; si se pasa -> 400
        error_messages={
            # Se usa cuando el JSON no trae la clave "nombre"
            "required": "El nombre es obligatorio.",
            # Se usa cuando "nombre" viene como "" (CharField no acepta vacío por defecto)
            "blank": "El nombre no puede estar vacío.",
        },
    )
    especie = serializers.CharField(
        max_length=50,  # Mismo límite que en el modelo
        error_messages={
            # Falta la clave "especie" en el JSON
            "required": "La especie es obligatoria.",
            # "especie" viene como cadena vacía
            "blank": "La especie no puede estar vacía.",
        },
    )
    edad = serializers.IntegerField(
        error_messages={
            # Falta la clave "edad" en el JSON
            "required": "La edad es obligatoria.",
            # El valor no se puede convertir a entero (ej. "tres")
            "invalid": "La edad debe ser un número entero.",
        },
    )

    # Meta indica qué modelo usar y qué campos exponer
    class Meta:
        # Modelo asociado: al guardar se crea/actualiza un Animal
        model = Animal
        # Campos que aparecen en el JSON de respuesta (y que se aceptan de entrada)
        fields = ["id", "nombre", "especie", "edad", "creado"]
        # Campos de solo lectura: salen en la respuesta pero se ignoran si el
        # cliente los envía (el id lo asigna MySQL y "creado" lo pone Django)
        read_only_fields = ["id", "creado"]

    # Validación personalizada de un campo: DRF busca métodos llamados
    # validate_<nombre_del_campo> y los ejecuta después de las validaciones básicas.
    # "value" ya es un int, porque IntegerField lo convirtió antes.
    def validate_edad(self, value):
        # Regla de negocio: la edad debe estar en un rango razonable
        if value < 0 or value > 100:
            # Lanzar ValidationError agrega el mensaje a errores["edad"] -> respuesta 400
            raise serializers.ValidationError("La edad debe estar entre 0 y 100.")
        # Si es válida, se devuelve el valor (es el que se guardará)
        return value
