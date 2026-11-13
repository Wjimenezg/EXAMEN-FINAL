# API REST de animales (Django REST Framework + MySQL)

## 1. Crear la base de datos en MySQL

```sql
CREATE DATABASE api_animales CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Luego abre `config/settings.py` y cambia `USER` y `PASSWORD` en `DATABASES` por los de tu MySQL.

## 2. Instalar dependencias

```bash
python -m venv venv
# Windows:     venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

## 3. Crear las tablas

```bash
python manage.py makemigrations animales
python manage.py migrate
```

## 4. Levantar el servidor en el puerto 8001

```bash
python manage.py runserver 8001
```

## 5. Hacer las seis pruebas

Abre **http://127.0.0.1:8001/** en el navegador. Ahí está el cliente HTTP.
Presiona los botones en orden y toma una captura después de cada uno:

| Botón              | Método | URL                     | Código esperado |
|--------------------|--------|-------------------------|-----------------|
| 1. Crear           | POST   | /api/animales/          | 201 Created     |
| 2. Listar          | GET    | /api/animales/          | 200 OK          |
| 3. Consultar ID    | GET    | /api/animales/<id>/     | 200 OK          |
| 4. Actualizar      | PUT    | /api/animales/<id>/     | 200 OK          |
| 5. Datos inválidos | POST   | /api/animales/          | 400 Bad Request |
| 6. Eliminar        | DELETE | /api/animales/<id>/     | 204 No Content  |

El cliente recuerda el id del registro que creaste en la prueba 1 y lo usa en
las pruebas 3, 4 y 6. Puedes editar la URL o el JSON antes de presionar Enviar.

Consejo: ejecuta la prueba 6 al final para que las pruebas 3 y 4 encuentren el registro.

## Endpoints

- `GET    /api/animales/`       listar
- `POST   /api/animales/`       crear (campos obligatorios: nombre, especie, edad)
- `GET    /api/animales/<id>/`  consultar por id
- `PUT    /api/animales/<id>/`  actualizar
- `DELETE /api/animales/<id>/`  eliminar
