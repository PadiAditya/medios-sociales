from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.post import Post
from utils.db import db

post_blueprint = Blueprint("posts", __name__)


@post_blueprint.route("/", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return jsonify([{"id": post.id, "content": post.content} for post in posts])

@post_blueprint.route("/", methods=["POST"])
@jwt_required
def create_post():
    user_id = get_jwt_identity()
    data = request.json
    new_post = Post(content=data["content"], user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created successfully"}), 201