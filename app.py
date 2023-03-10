from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)

#conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#tabla de registro
class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False )
    pasword = db.Column(db.String(80), nullable=False )
    email = db.Column(db.String(100), nullable=False)

#direccion de la pagina
@app.route("/", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        hashed_pw = generate_password_hash(request.form['pasword'], method="sha256")
        new_user = users(username=request.form["username"], pasword=hashed_pw)
        emails = users(email=request.form["email"])

        #almacenando en la base de datos
        db.session.add(new_user)
        db.session.commit()
        return render_template("sing.html")
    return render_template("sing.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = users.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(user.pasword, request.form["pasword"]):

            return redirect(url_for("myblokchain"))
        return render_template('Try again')
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
