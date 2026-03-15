from flask import Blueprint, request, jsonify
from models import db, Task
from schemas import TaskSchema
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import NotFound

bp = Blueprint('tasks', __name__, url_prefix='/api')
task_schema = TaskSchema()


def validation_error_response(errors):
    return jsonify({'error': 'Validation failed', 'errors': errors}), 400

@bp.route('/tasks', methods=['GET'])
def list_tasks():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 50, type=int)
        status = request.args.get('status')
        priority = request.args.get('priority')
        
        query = Task.query
        if status:
            query = query.filter_by(status=status)
        if priority:
            query = query.filter_by(priority=priority)
        
        tasks = query.order_by(Task.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
        return jsonify({
            'tasks': task_schema.dump(tasks.items, many=True),
            'total': tasks.total,
            'page': tasks.page,
            'pages': tasks.pages
        }), 200
    except Exception:
        return jsonify({'error': 'Failed to fetch tasks'}), 500

@bp.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json(silent=True) or {}
        errors = task_schema.validate(data)
        if errors:
            return validation_error_response(errors)
        task = Task(
            title=data['title'].strip(),
            description=data.get('description', '').strip(),
            status=data.get('status', 'pending'),
            priority=data.get('priority', 'medium')
        )
        db.session.add(task)
        db.session.commit()
        return task_schema.dump(task), 201
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Database error'}), 500
    except Exception:
        return jsonify({'error': 'Failed to create task'}), 500

@bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
        return task_schema.dump(task)
    except NotFound:
        return jsonify({'error': 'Task not found'}), 404

@bp.route('/tasks/<int:task_id>', methods=['PUT', 'PATCH'])
def update_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
        data = request.get_json(silent=True) or {}
        errors = task_schema.validate(data, partial=True)
        if errors:
            return validation_error_response(errors)
        if 'title' in data:
            task.title = data['title'].strip()
        if 'description' in data:
            task.description = data['description'].strip()
        if 'status' in data:
            task.status = data['status']
        if 'priority' in data:
            task.priority = data['priority']
        db.session.commit()
        return task_schema.dump(task)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Database error'}), 500
    except NotFound:
        return jsonify({'error': 'Task not found'}), 404
    except Exception:
        return jsonify({'error': 'Failed to update task'}), 500

@bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Database error'}), 500
    except NotFound:
        return jsonify({'error': 'Task not found'}), 404
    except Exception:
        return jsonify({'error': 'Failed to delete task'}), 500
