from flask import Blueprint

users = Blueprint('users', __name__)

import flaskblog.users.routes