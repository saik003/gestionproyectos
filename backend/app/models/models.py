from app import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date, nullable=False)
    area = db.Column(db.String(150))
    priority = db.Column(db.String(20))
    end_date = db.Column(db.Date)
    estimated_hours = db.Column(db.Float)
    completed_hours = db.Column(db.Float, default=0)
    status = db.Column(db.String(20), default='active')  # active, inactive
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    project = db.relationship('Project', back_populates='tasks')
    assignee = db.relationship('User', foreign_keys=[assigned_to], back_populates='assigned_tasks')
    creator = db.relationship('User', foreign_keys=[created_by], back_populates='created_tasks')
    daily_records = db.relationship('DailyRecord', back_populates='task', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start_date': self.start_date.strftime('%Y-%m-%d') if self.start_date else None,
            'end_date': self.end_date.strftime('%Y-%m-%d') if self.end_date else None,
            'estimated_hours': self.estimated_hours,
            'completed_hours': self.completed_hours,
            'status': self.status,
            'project_id': self.project_id,
            'assigned_to': self.assigned_to,
            'created_by': self.created_by,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'project_name': self.project.name if self.project else None,
            'assignee_name': self.assignee.name if self.assignee else None,
            'creator_name': self.creator.name if self.creator else None,
            'area': self.area,
            'priority': self.priority
        }

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    role = db.Column(db.String(50))
    active = db.Column(db.Boolean, default=True)
    
    # Relaciones
    assigned_tasks = db.relationship('Task', foreign_keys='Task.assigned_to', back_populates='assignee')
    created_tasks = db.relationship('Task', foreign_keys='Task.created_by', back_populates='creator')
    daily_records = db.relationship('DailyRecord', back_populates='user')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'active': self.active
        }

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    active = db.Column(db.Boolean, default=True)
    
    # Relaciones
    tasks = db.relationship('Task', back_populates='project', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.strftime('%Y-%m-%d') if self.start_date else None,
            'end_date': self.end_date.strftime('%Y-%m-%d') if self.end_date else None,
            'active': self.active
        }

class DailyRecord(db.Model):
    __tablename__ = 'daily_records'
    
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hours = db.Column(db.Float, nullable=False)
    comments = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    task = db.relationship('Task', back_populates='daily_records')
    user = db.relationship('User', back_populates='daily_records')
    
    def to_dict(self):
        return {
            'id': self.id,
            'task_id': self.task_id,
            'user_id': self.user_id,
            'date': self.date.strftime('%Y-%m-%d'),
            'hours': self.hours,
            'comments': self.comments,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'task_title': self.task.title if self.task else None,
            'user_name': self.user.name if self.user else None
        }
