from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app=app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


# Providing a user_loader callback that is used to reload the user object from the user id stored in the session.
# Here, session is the activity done in the website, when user goes to the website, then there is the begining of the session.
# So, here we are talking about the id that is entered by the user while registering with the website.

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # It will help me to get the user_id in the string form.
    # It will be used in the user_loader callback to return user object from the user id.
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

 

# LoginManager() class contains the code that makes the application and flask-login to work together.
# With the help of it, we can load the users from the id stored in the database.
# We can decide where to send the user when they need to login.

# Configuring application with the login manager.

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)
# current_user is the user that is currently working on the website.
# is_authenticated is an attribute that checks whether the user is verified or not. It returns boolean value.


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = db.session.execute(db.select(User).where(User.email==request.form['email'])).scalar()
        if user:
            flash("You've already signed up with this email, log in instead!")
            return redirect(url_for('login'))
        password_hash = generate_password_hash(request.form['password'], method="pbkdf2:sha256", salt_length=8)
        user = User(email=request.form['email'], password=password_hash, name=request.form['name'])
        db.session.add(user)
        db.session.commit()
        login_user(user)
        # user that is registered will be logged into the website.
        return redirect(url_for('secrets'))
    
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_email = request.form.get("email")
        login_password = request.form.get("password")
        user = db.session.execute(db.select(User).where(User.email==login_email)).scalar()
        # Here, we are obtaining the user that is trying to log into the website.
        # First, we check that the email that is entered into the login form is in the database or not.
        if user:
            if check_password_hash(pwhash=user.password, password=login_password):
                login_user(user=user)
                return redirect(url_for('secrets'))
            else:
                flash("Password incorrect, please try again.")
        else:
            flash("That email does not exist, Please try again.")
        
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", logged_in=current_user.is_authenticated, name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home', logged_in=current_user.is_authenticated))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory="static", path="files/cheat_sheet.pdf", as_attachment=True)
    # Using send_from_directory() in order to send the file from the folder using flask.
    # First, you need to mention the directory/folder in which the required file is stored.
    # Then, file path relative to the directory.
    # as_attachment=True keyword argument. 


if __name__ == "__main__":
    app.run(debug=True)
