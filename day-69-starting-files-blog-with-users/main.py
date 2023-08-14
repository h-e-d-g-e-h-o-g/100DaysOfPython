from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm


'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app=app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None
            )

# Gravatar images are used for providing avatar images for blog commentators.
# For each email users, avatar would be provided.


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

def admin_only(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        admin_user = db.session.get(User, 1)
        if admin_user != current_user:
            return abort(403)
        else:
            return function(*args, **kwargs)
    return decorated_function

# CONFIGURE TABLES
# TODO: Create a User table for all your registered users. 
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    # This property "posts" will act as a list of BlogPost objects that attached to each user.
    # Here, author represents the property in the BlogPost class.
    # Through this, we can easily identify the post that is written by the current user 
    # through author property in the BlogPost object.
    comments = relationship("Comment", back_populates="writer")
    # It will return a list of all the comment objects that user has written.


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # Here, we create a ForeignKey author_id that is primary key of User table.
    # ForeignKey helps in building relationship between tables, the one with foreign key is child.
    # The one whose primary key is in child is called parent.
    # Here, "users" is the name of the User table.
    author = relationship("User", back_populates="posts")
    # Here, we are creating the referance to the user object, and posts is the property of User table.
    # Here, we can easily identify the author of a particular post through posts property in the User table.
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    post_comments = relationship("Comment", back_populates="parent_post")
    # It will return the list of all the comments that is written on a post. 

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    # Here, text property represents the text that is entered into the comment section.
    writer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # Here, we can identify the writer who has written the comment through his/her id.
    writer = relationship("User", back_populates="comments")
    # A user(writer) can write multiple comments
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    # Here, we can identify the specific post on which the comment is written.
    parent_post = relationship("BlogPost", back_populates="post_comments")
    # A post will have multiple comments.
    text = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        email = register_form.email.data
        user = db.session.execute(db.select(User).where(User.email==email)).scalar()
        if not user:
            password = register_form.password.data
            name = register_form.name.data
            user = User(email=email, 
                        password=generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8), 
                        name=name
                    )
            db.session.add(user)
            db.session.commit()
            login_user(user=user)
            return redirect(url_for('get_all_posts'))
        
        else:
            flash("You've already signed up with that email, log in instead.")
            return redirect(url_for('login'))

    return render_template("register.html", form=register_form, logged_in=current_user.is_authenticated)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = db.session.execute(db.select(User).where(User.email==email)).scalar()
        if not user:
            flash("That email does not exist, please try again!")
        elif not check_password_hash(pwhash=user.password, password=password):
            flash("Password incorrect, please try again!")
        else:
            login_user(user=user)
            print(current_user.name)
            return redirect(url_for('get_all_posts'))
            
    return render_template("login.html", form=login_form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    admin_login = False
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    admin_user = db.session.get(User, 1)
    if admin_user == current_user:
        admin_login = True
    return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated, admin_login=admin_login)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for('login'))
        
        post_comment = comment_form.comment.data
        comment_obj = Comment(writer_id=current_user.id, post_id=post_id, text=post_comment)
        # Here, if the user is authenticated, then we will add the comment written by him or her into the comment table.
        db.session.add(comment_obj)
        db.session.commit()

    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post, form=comment_form, logged_in=current_user.is_authenticated, comments=requested_post.post_comments)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
