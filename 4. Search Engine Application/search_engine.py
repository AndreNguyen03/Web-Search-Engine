from flask import Flask, render_template

app = Flask(__name__, template_folder="./static/")


@app.route("/")
@app.route("/a")
def a():
    return render_template("A.html")

@app.route("/b")
def b():
    return render_template("B.html")

@app.route("/c")
def c():
    return render_template("C.html")

@app.route("/d")
def d():
    return render_template("D.html")

@app.route("/e")
def e():
    return render_template("E.html")


@app.route("/about")
def about_page():
    return "<p>About ccon cac!</p>"

