from flask import Blueprint, request, jsonify
from app.models.models import Project
from app import db
from datetime import datetime

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects])

@projects_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify(project.to_dict())

@projects_bp.route('/', methods=['POST'])
def create_project():
    data = request.json
    
    # Convertir fechas de string a objeto Date
    start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d').date() if data.get('start_date') else None
    end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d').date() if data.get('end_date') else None
    
    new_project = Project(
        name=data.get('name'),
        description=data.get('description'),
        start_date=start_date,
        end_date=end_date,
        active=data.get('active', True)
    )
    
    db.session.add(new_project)
    db.session.commit()
    
    return jsonify(new_project.to_dict()), 201

@projects_bp.route('/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    data = request.json
    
    if 'name' in data:
        project.name = data['name']
    if 'description' in data:
        project.description = data['description']
    if 'start_date' in data and data['start_date']:
        project.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
    if 'end_date' in data and data['end_date']:
        project.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
    if 'active' in data:
        project.active = data['active']
    
    db.session.commit()
    return jsonify(project.to_dict())

@projects_bp.route('/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'success'}), 200
