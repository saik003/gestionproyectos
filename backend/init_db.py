from app import create_app, db
from app.models.models import User, Project, Task, DailyRecord
import json
import os
from datetime import datetime

def init_db():
    """Inicializa la base de datos con datos de localStorage si existen"""
    app = create_app()
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        
        # Verificar si ya hay datos en la base de datos
        if User.query.first() is not None:
            print("La base de datos ya está inicializada.")
            return
        
        # Buscar el archivo HTML principal
        html_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'index.html')
        
        # Función para extraer datos de localStorage desde el HTML
        def extract_local_storage_data(html_content, key):
            try:
                # Esta es una forma simple, podría necesitar un parser HTML real para casos complejos
                if f"localStorage.getItem('{key}')" in html_content:
                    return []
                return []
            except:
                return []
        
        # Intentar cargar datos existentes desde localStorage (este es un ejemplo básico)
        # En una implementación real, podrías proporcionar un JSON con los datos iniciales
        
        # Crear usuarios iniciales si no hay datos
        if User.query.count() == 0:
            default_users = [
                User(name="Administrador", email="admin@example.com", role="Admin", active=True),
                User(name="Usuario Demo", email="demo@example.com", role="Usuario", active=True)
            ]
            db.session.add_all(default_users)
            db.session.commit()
            print("Usuarios iniciales creados.")
        
        # Crear proyectos iniciales
        if Project.query.count() == 0:
            default_projects = [
                Project(name="Proyecto Demo", description="Un proyecto de demostración", 
                        start_date=datetime.now().date(), active=True)
            ]
            db.session.add_all(default_projects)
            db.session.commit()
            print("Proyectos iniciales creados.")
        
        print("Base de datos inicializada correctamente.")

if __name__ == "__main__":
    init_db()
