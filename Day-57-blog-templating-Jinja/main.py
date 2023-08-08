from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()

@app.route('/')
def home():
    return "<h1>Welcome to my Blog Website</h1>\
            <a href='/blogs'>Go to my Blogs page!</a>"

@app.route('/blogs')
def listing_blogs():
    return render_template("index.html", posts=all_posts)

@app.route(f"/post/<int:id_num>")
def get_blog(id_num):
    print(id_num)
    blog_post = Post(id_num, all_posts)
    blog_title = blog_post.blog_title
    blog_subtitle = blog_post.blog_subtitle
    blog_body = blog_post.blog_body
    return render_template("post.html", post_title=blog_title, post_subtitle=blog_subtitle, post_body=blog_body)

if __name__ == "__main__":
    app.run(debug=True)
