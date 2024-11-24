from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from utils.db import db

# Initialize Flask app
app = Flask(__name__)
CORS(app)

app.config.from_object("config.Config")

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from routes.auth import auth_blueprint
from routes.post import post_blueprint
from routes.comment import comment_blueprint
from routes.user import user_blueprint

app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(post_blueprint, url_prefix="/posts")
app.register_blueprint(comment_blueprint, url_prefix="/comments")
app.register_blueprint(user_blueprint, url_prefix="/users")


if __name__ == "__main__":
    app.run(debug=True)