from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from app import app

#cofiguraciones de sql
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)

#creacion de la tabla usuario
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(500), nullable=False)
    email = db.Column(db.string(500), unique=True, nullable=False)
    password = db.Column(db.string(128), nullable=False)
    phone = db.Column(db.string(212), unique=True, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_passsword(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Users.query.get(id)

    @staticmethod
    def get_by_email(email):
        return Users.query.filter_by(email=email).first()
