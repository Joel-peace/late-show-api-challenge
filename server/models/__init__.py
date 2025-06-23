from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .guest import Guest
from .user import User
