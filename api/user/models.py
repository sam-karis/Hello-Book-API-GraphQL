from sqlalchemy import (Column, String, Integer)
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

from api.database import Base, Utility

class User(Base, Utility):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    username = Column(String(60), nullable=False, unique=True)
    password_hash = Column(String(200))

    def hash_password(self, password):
        """Hash password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check password given is valid."""
        return check_password_hash(self.password_hash, password)
