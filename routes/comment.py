from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.comment import Comment
from utils.db import db

comment_blueprint = Blueprint("comment", __name__)


@comment_blueprint.route("/", methods=["GET"])
def get_comments():
    comments = Comment.query.all()
    return jsonify([{"id": comment.id, "content": comment.content} for comment in comments])

@comment_blueprint.route("/", methods=["POST"])
@jwt_required
def create_comment():
    user_id = get_jwt_identity()
    data = request.json
    new_comment = Comment(content=data["content"], user_id=user_id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comment created successfully"}), 201