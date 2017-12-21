from flask import Flask, render_template, redirect, url_for, request
from models import *

app = Flask(__name__)

@app.before_request
def before_request():
	initialize_db()

@app.teardown_request
def teardown_request(exception):
	db.close()

@app.route("/")
def home():
	return render_template("home.html", posts=Post.select().order_by(Post.date))

@app.route("/new_post/")
def new_post():
	return render_template("new_post.html")

@app.route("/create/", methods=["POST"])
def create_post():
	Post.create(
		author = request.form['nickname'],
		post = request.form['text']
	)
	return redirect(url_for("home"))


if __name__ == "__main__":
	app.run(debug=True)