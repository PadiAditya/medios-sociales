from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from utils.db import db

user_blueprint = Blueprint("users", __name__)


@user_blueprint.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.username, "email": user.email} for user in users])
