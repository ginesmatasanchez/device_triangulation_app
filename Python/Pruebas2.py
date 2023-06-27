from flask import Blueprint, render_template

Pruebas2 = Blueprint("Pruebas2", __name__, template_folder="templates")

@Pruebas2.route("/home")
def home():
    return render_template("home.html")

@Pruebas2.route("/test")
def test():
    return "<h1>TEST</h1>"
