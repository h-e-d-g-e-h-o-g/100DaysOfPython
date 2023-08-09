from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

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
ckeditor = CKEditor()
# Creating a CKEditor object 
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)
ckeditor.init_app(app=app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    results = db.session.execute(db.select(BlogPost))
    posts = results.scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.get(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
class AddPostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    name = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired()])
    content = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit_post = SubmitField(label="SUBMIT POST")

@app.route("/new-post", methods=["GET", "POST"])
def add_post():
    add_post_form = AddPostForm()
    heading = "New Post"
    if request.method == "POST":
        if add_post_form.validate_on_submit():
            new_blog_post = BlogPost(title=add_post_form.title.data, 
                                     subtitle=add_post_form.subtitle.data,
                                     date=date.today().strftime("%B %d, %Y"),
                                     body=add_post_form.content.data,
                                     author=add_post_form.name.data,
                                     img_url=add_post_form.img_url.data
                            )
            db.session.add(new_blog_post)
            db.session.commit()

            return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=add_post_form, post_heading=heading)
# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    edit_post = db.session.get(BlogPost, post_id)
    edit_post_form = AddPostForm(title=edit_post.title,
                                 subtitle=edit_post.subtitle,
                                 name=edit_post.author,
                                 img_url=edit_post.img_url,
                                 content=edit_post.body,
                                 )
    # In order to auto-populate the form fields we can set the default value to the AddPostForm's attributes.
    
    heading = "Edit Post"
    if edit_post_form.validate_on_submit():
        edit_post.title = edit_post_form.title.data
        edit_post.subtitle = edit_post_form.subtitle.data
        edit_post.body = edit_post_form.content.data
        edit_post.author = edit_post_form.name.data
        edit_post.img_url = edit_post_form.img_url.data
        db.session.commit()

        return redirect(url_for('show_post', post_id=post_id))
    
    return render_template("make-post.html", form=edit_post_form, post_heading=heading)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_delete = db.session.get(BlogPost, post_id)
    db.session.delete(post_delete)
    db.session.commit()
    
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
