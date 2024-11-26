from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.post import Post
from models.comment import Comment
from utils.db import db

post_blueprint = Blueprint("posts", __name__)


@post_blueprint.route("/", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return jsonify([{"id": post.id, "content": post.content} for post in posts])

@post_blueprint.route("/<int:post_id>/comments", methods=["GET"])
def get_comments(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'message': f"Post {post_id} not found"}), 404
    
    comments = Comment.query.filter_by(post_id=post_id)
    response = [{
        "id": comment.id,
        "content": comment.content,
        "user_id": comment.user_id,
        "created_at": comment.created_at
    } for comment in comments]
    return jsonify(response), 200

@post_blueprint.route("/", methods=["POST"])
@jwt_required()
def create_post():
    user_id = get_jwt_identity()
    data = request.json
    new_post = Post(content=data["content"], user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully"}), 201

@post_blueprint.route("/<int:post_id>", methods=["POST"])
@jwt_required()
def add_comment(post_id):
    user_id = get_jwt_identity()
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'message': f"Post {post_id} not found"}), 404
    data = request.json
    content = data.get("content")
    if not content:
        return jsonify({"message": "Content is required"}), 400
    
    new_comment = Comment(content=content, user_id=user_id, post_id=post_id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comment created successfully"}), 201


