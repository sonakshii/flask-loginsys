from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:test@localhost/loginsignup'
db = SQLAlchemy(app)


class Userinfo(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(80), nullable=False)
    Email = db.Column(db.String(120), nullable=False)
    Password = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["psw"]
        login = Userinfo.query.filter_by(Username=uname, Password=passw).first()
        if login is None:
            return render_template('loginerror.html')
        return render_template('loginsucces.html')
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if (request.method == 'POST'):
        username = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('psw')
        entry = Userinfo(Username=username, Email=email, Password=password)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("signupsucces"))
    return render_template("signup.html")

@app.route('/signupsucces')
def signupsucces():
    return render_template('signupsucces.html')

@app.route('/loginerror')
def loginerror():
    return render_template('loginerror.html')

@app.route('/loginsucces')
def loginsucces():
    return render_template('loginsucces.html')

app.run(debug=True)