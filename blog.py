from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    footy_managers = ["pep", "jose", "fergie"]
    first_name = "Tanmay"
    stuff = "This is <strong>Bold</strong> text"
    return render_template("index.html", first_name=first_name, stuff=stuff, footy_managers=footy_managers)

#http://localhost:5000/

@app.route('/greet/<name>')
def greet_user(name):
    return render_template("greet_user.html", user_name=name)
#http://localhost:5000/greet/Tanmay

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)