from flask import Blueprint, request, jsonify
from models import db, Task, Comment
from schemas import CommentSchema
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import NotFound

bp = Blueprint('comments', __name__, url_prefix='/api')

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)


def validation_error_response(errors):
    return jsonify({'error': 'Validation failed', 'errors': errors}), 400

@bp.route('/tasks/<int:task_id>/comments', methods=['POST'])
def create_comment(task_id):
    try:
        Task.query.get_or_404(task_id)
        json_data = request.get_json(silent=True) or {}
        json_data['task_id'] = task_id
        errors = comment_schema.validate(json_data)
        if errors:
            return validation_error_response(errors)
        comment = Comment(
            task_id=task_id,
            author=json_data['author'].strip(),
            content=json_data['content'].strip()
        )
        db.session.add(comment)
        db.session.commit()
        return comment_schema.dump(comment), 201
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Database error'}), 500
    except NotFound:
        return jsonify({'error': 'Task not found'}), 404
    except Exception:
        return jsonify({'error': 'Failed to create comment'}), 500

@bp.route('/tasks/<int:task_id>/comments', methods=['GET'])
def list_comments(task_id):
    try:
        Task.query.get_or_404(task_id)
        q = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at.asc())
        return comments_schema.dump(q.all())
    except NotFound:
        return jsonify({'error': 'Task not found'}), 404
    except Exception:
        return jsonify({'error': 'Failed to fetch comments'}), 500

@bp.route('/tasks/<int:task_id>/comments/<int:comment_id>', methods=['GET'])
def get_comment(task_id, comment_id):
    try:
        Task.query.get_or_404(task_id)
        comment = Comment.query.filter_by(task_id=task_id, id=comment_id).first_or_404()
        return comment_schema.dump(comment)
    except NotFound:
        return jsonify({'error': 'Comment not found'}), 404

@bp.route('/tasks/<int:task_id>/comments/<int:comment_id>', methods=['PUT', 'PATCH'])
def update_comment(task_id, comment_id):
    try:
        Task.query.get_or_404(task_id)
        comment = Comment.query.filter_by(task_id=task_id, id=comment_id).first_or_404()
        json_data = request.get_json(silent=True) or {}
        errors = comment_schema.validate(
            {**json_data, 'task_id': task_id},
            partial=request.method == 'PATCH',
        )
        if errors:
            return validation_error_response(errors)
        if 'author' in json_data:
            comment.author = json_data['author'].strip()
        if 'content' in json_data:
            comment.content = json_data['content'].strip()
        db.session.commit()
        return comment_schema.dump(comment)
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Database error'}), 500
    except NotFound:
        return jsonify({'error': 'Comment not found'}), 404
    except Exception:
        return jsonify({'error': 'Failed to update comment'}), 500

@bp.route('/tasks/<int:task_id>/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(task_id, comment_id):
    try:
        Task.query.get_or_404(task_id)
        comment = Comment.query.filter_by(task_id=task_id, id=comment_id).first_or_404()
        db.session.delete(comment)
        db.session.commit()
        return '', 204
    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({'error': 'Database error'}), 500
    except NotFound:
        return jsonify({'error': 'Comment not found'}), 404
    except Exception:
        return jsonify({'error': 'Failed to delete comment'}), 500
