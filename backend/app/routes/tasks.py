from flask import Blueprint, request, jsonify
from flask import Blueprint, request, jsonify
from app.models.models import Task, DailyRecord
from app import db
from datetime import datetime

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

@tasks_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task.to_dict())

@tasks_bp.route('/', methods=['POST'])
def create_task():
    data = request.json
    
    # Convertir fechas de string a objeto Date
    start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d').date() if data.get('start_date') else None
    end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d').date() if data.get('end_date') else None
    
    new_task = Task(
        title=data.get('title'),
        description=data.get('description'),
        start_date=start_date,
        area=data.get('area'),
        end_date=end_date,
        estimated_hours=data.get('estimated_hours'),
        project_id=data.get('project_id'),
        assigned_to=data.get('assigned_to'),
        created_by=data.get('created_by'),
        status='active',
        priority=data.get('priority')
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify(new_task.to_dict()), 201

@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    
    # Actualizar campos
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'start_date' in data and data['start_date']:
        task.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()
    if 'end_date' in data and data['end_date']:
        task.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date()
    if 'estimated_hours' in data:
        task.estimated_hours = data['estimated_hours']
    if 'status' in data:
        task.status = data['status']
    if 'project_id' in data:
        task.project_id = data['project_id']
    if 'assigned_to' in data:
        task.assigned_to = data['assigned_to']
    if 'area' in data:
        task.area = data['area']
    if 'priority' in data:
        task.priority = data['priority']
    
    db.session.commit()
    return jsonify(task.to_dict())

@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Tarea eliminada correctamente'}), 200

@tasks_bp.route('/<int:task_id>/status', methods=['PUT'])
def update_task_status(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    
    if 'status' in data:
        task.status = data['status']
    
    db.session.commit()
    return jsonify(task.to_dict())
