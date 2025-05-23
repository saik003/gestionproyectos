# Backend API para Sistema de Seguimiento IT

Este es el backend API desarrollado con Flask y SQLite para el Sistema de Seguimiento IT.

## Requisitos

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-CORS

## Instalación

1. Instalar las dependencias:

```
pip install -r requirements.txt
```

2. Inicializar la base de datos:

```
python init_db.py
```

3. Ejecutar la aplicación:

```
python run.py
```

## Estructura API

El API expone los siguientes endpoints:

### Tareas
- `GET /api/tasks/` - Obtener todas las tareas
- `GET /api/tasks/<id>` - Obtener una tarea específica
- `POST /api/tasks/` - Crear una nueva tarea
- `PUT /api/tasks/<id>` - Actualizar una tarea existente
- `DELETE /api/tasks/<id>` - Eliminar una tarea
- `PUT /api/tasks/<id>/status` - Actualizar el estado de una tarea

### Usuarios
- `GET /api/users/` - Obtener todos los usuarios
- `GET /api/users/<id>` - Obtener un usuario específico
- `POST /api/users/` - Crear un nuevo usuario
- `PUT /api/users/<id>` - Actualizar un usuario existente
- `DELETE /api/users/<id>` - Eliminar un usuario

### Proyectos
- `GET /api/projects/` - Obtener todos los proyectos
- `GET /api/projects/<id>` - Obtener un proyecto específico
- `POST /api/projects/` - Crear un nuevo proyecto
- `PUT /api/projects/<id>` - Actualizar un proyecto existente
- `DELETE /api/projects/<id>` - Eliminar un proyecto

### Registros Diarios
- `GET /api/daily-records/` - Obtener todos los registros diarios
- `GET /api/daily-records/task/<task_id>` - Obtener registros por tarea
- `GET /api/daily-records/user/<user_id>` - Obtener registros por usuario
- `POST /api/daily-records/` - Crear un nuevo registro diario
- `PUT /api/daily-records/<id>` - Actualizar un registro existente
- `DELETE /api/daily-records/<id>` - Eliminar un registro diario
