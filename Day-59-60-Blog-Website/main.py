from flask import Flask, render_template, request
import requests, smtplib

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/b5b193e7bbeec6c3000f")
blog_posts = response.json()

my_email = "raholverma20@gmail.com"
my_password = "fttwxryohmtkqraa"

@app.route("/")
def home():
    # url_for('static', filename='css/styles.css')
    return render_template("index.html", posts=blog_posts)

@app.route("/about")
def about():
    return render_template("about.html")
 
@app.route("/contact", methods=["GET", "POST"])
def contact():
    heading = "Contact Me"
    if request.method == "POST": 
        heading =  "Successfully sent your message"
        user_name = request.form['name']
        user_email = request.form['email']
        user_phone = request.form['phone']
        user_message = request.form['message']
        message = f"Name: {user_name}\nEmail: {user_email}\nPhone: {user_phone}\nMessage: {user_message}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=user_email, to_addrs=my_email, msg=f"Subject:New Message\n\n{message}")
            
    return render_template("contact.html", contact_heading=heading)

@app.route("/post/<int:post_id>")
def get_post(post_id):
    print(post_id)
    post_title = blog_posts[post_id-1]['title']
    post_subtitle = blog_posts[post_id-1]['subtitle']
    post_body = blog_posts[post_id-1]['body']
    post_date = blog_posts[post_id-1]['date']
    post_img_path = blog_posts[post_id-1]['img_path']
    return render_template("post.html", title=post_title, subtitle=post_subtitle, body=post_body, date=post_date, img_path=post_img_path)

if __name__ == "__main__":
    app.run(debug=True)