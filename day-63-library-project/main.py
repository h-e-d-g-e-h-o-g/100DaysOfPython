from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

db.init_app(app=app)

with app.app_context():
    db.create_all()   


@app.route('/')
def home():
    books_obj = db.session.execute(db.select(Books).order_by('title')).scalars() 
    all_books = []
    for book in books_obj:
        all_books.append(book)

    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book = Books(title=request.form['book'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    book_edit = db.get_or_404(Books, id)
    if request.method == "POST":
        book_edit.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("edit.html", book=book_edit)

@app.route('/delete/<int:id>')
def delete(id):
    book_delete = db.get_or_404(Books, id)
    db.session.delete(book_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
