from app import create_app, db
from app.models.models import Task, User, Project, DailyRecord

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 
        'Task': Task, 
        'User': User, 
        'Project': Project, 
        'DailyRecord': DailyRecord
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
