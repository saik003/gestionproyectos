from flask import Blueprint, request, jsonify
from app.models.models import DailyRecord, Task
from app import db
from datetime import datetime

daily_records_bp = Blueprint('daily_records', __name__)

@daily_records_bp.route('/', methods=['GET'])
def get_daily_records():
    daily_records = DailyRecord.query.all()
    return jsonify([record.to_dict() for record in daily_records])

@daily_records_bp.route('/task/<int:task_id>', methods=['GET'])
def get_daily_records_by_task(task_id):
    records = DailyRecord.query.filter_by(task_id=task_id).all()
    return jsonify([record.to_dict() for record in records])

@daily_records_bp.route('/user/<int:user_id>', methods=['GET'])
def get_daily_records_by_user(user_id):
    records = DailyRecord.query.filter_by(user_id=user_id).all()
    return jsonify([record.to_dict() for record in records])

@daily_records_bp.route('/<int:record_id>', methods=['GET'])
def get_daily_record(record_id):
    record = DailyRecord.query.get_or_404(record_id)
    return jsonify(record.to_dict())

@daily_records_bp.route('/', methods=['POST'])
def create_daily_record():
    data = request.json
    
    # Convertir fecha de string a objeto Date
    record_date = datetime.strptime(data.get('date'), '%Y-%m-%d').date() if data.get('date') else datetime.utcnow().date()
    
    new_record = DailyRecord(
        task_id=data.get('task_id'),
        user_id=data.get('user_id'),
        date=record_date,
        hours=data.get('hours', 0),
        comments=data.get('comments', '')
    )
    
    db.session.add(new_record)
    
    # Actualizar horas completadas en la tarea
    if new_record.task_id:
        task = Task.query.get(new_record.task_id)
        if task:
            task.completed_hours = (task.completed_hours or 0) + new_record.hours
    
    db.session.commit()
    
    return jsonify(new_record.to_dict()), 201

@daily_records_bp.route('/<int:record_id>', methods=['PUT'])
def update_daily_record(record_id):
    record = DailyRecord.query.get_or_404(record_id)
    data = request.json
    
    # Guardar el valor anterior de horas para actualizar el total en la tarea
    old_hours = record.hours
    
    if 'task_id' in data:
        record.task_id = data['task_id']
    if 'user_id' in data:
        record.user_id = data['user_id']
    if 'date' in data and data['date']:
        record.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
    if 'hours' in data:
        record.hours = data['hours']
    if 'comments' in data:
        record.comments = data['comments']
    
    # Actualizar horas completadas en la tarea
    if record.task_id and 'hours' in data:
        task = Task.query.get(record.task_id)
        if task:
            task.completed_hours = (task.completed_hours or 0) - old_hours + record.hours
    
    db.session.commit()
    return jsonify(record.to_dict())

@daily_records_bp.route('/<int:record_id>', methods=['DELETE'])
def delete_daily_record(record_id):
    record = DailyRecord.query.get_or_404(record_id)
    
    # Actualizar horas completadas en la tarea
    if record.task_id:
        task = Task.query.get(record.task_id)
        if task:
            task.completed_hours = (task.completed_hours or 0) - record.hours
    
    db.session.delete(record)
    db.session.commit()
    return jsonify({'message': 'Registro diario eliminado correctamente'}), 200
