# models.py: define la estructura de los datos. Cada clase Model se convierte
# en una tabla de la base de datos y cada atributo en una columna.

# models contiene la clase base Model y los tipos de campo (CharField, etc.)
from django.db import models


# Modelo Animal -> tabla "animales" en MySQL
class Animal(models.Model):

    # Texto corto de hasta 100 caracteres -> VARCHAR(100) NOT NULL
    nombre = models.CharField(max_length=100)
    # Texto corto de hasta 50 caracteres -> VARCHAR(50) NOT NULL
    especie = models.CharField(max_length=50)
    # Entero que no acepta negativos -> INT UNSIGNED NOT NULL
    edad = models.PositiveIntegerField()
    # Fecha y hora de creación; auto_now_add la llena sola al insertar el registro
    creado = models.DateTimeField(auto_now_add=True)

    # Meta guarda opciones del modelo que no son columnas
    class Meta:
        # Nombre exacto de la tabla (si no, Django usaría "animales_animal")
        db_table = "animales"
        # Orden por defecto de las consultas: por id ascendente
        ordering = ["id"]

    # Texto que representa al objeto (se ve en el admin y en la consola)
    def __str__(self):
        return f"{self.nombre} ({self.especie})"
