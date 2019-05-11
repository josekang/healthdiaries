from flask import Flask, render_template
from myproject import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sixeight")
def sixeight():
    return render_template("6-8.html")

@app.route("/nineeleven")
def nineeleven():
    return render_template("9-11.html")

@app.route("/twelvetwentyfour")
def twelvetwentyfour():
    return render_template("12-24.html")

@app.route("/twentyfivefiftynine")
def twentyfivefiftynine():
    return render_template("25-59.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
