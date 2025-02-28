from flask import Blueprint, jsonify, request
from app import db
from app.models.content import Content

content_bp = Blueprint('content', __name__)

@content_bp.route('/api/content', methods=['GET'])
def get_content():
    try:
        content_list = Content.query.order_by(Content.created_at.desc()).all()
        return jsonify({
            'status': 'success',
            'data': [content.to_dict() for content in content_list]
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@content_bp.route('/api/content/<int:content_id>/vote', methods=['POST'])
def vote_content(content_id):
    try:
        vote_type = request.json.get('type')
        content = Content.query.get_or_404(content_id)
        
        if vote_type == 'upvote':
            content.upvotes += 1
        elif vote_type == 'downvote':
            content.downvotes += 1
            
        db.session.commit()
        return jsonify({
            'status': 'success',
            'data': content.to_dict()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500