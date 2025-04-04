from flask import Blueprint, jsonify, request
from model.models import SocialMediaPost, db

api_bp = Blueprint('api', __name__)

@api_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = SocialMediaPost.query.all()
    return jsonify([post.to_dict() for post in posts])

@api_bp.route('/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    post = SocialMediaPost(
        platform=data.get('platform'),
        content=data.get('content'),
        likes=data.get('likes', 0),
        comments=data.get('comments', 0),
        shares=data.get('shares', 0)
    )
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201