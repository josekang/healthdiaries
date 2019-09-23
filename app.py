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

@app.route("/child")
def child():
    return render_template("child.html")

@app.route("/matnut")
def matnut():
    return render_template("matnut.html")

@app.route("/mealfreq")
def mealfreq():
    return render_template("mealfreq.html")

@app.route("/amocfcfn")
def amocfcfn():
    return render_template("amocfcfn.html")

@app.route("/useofvit")
def useofvit():
    return render_template("useofvit.html")

@app.route("/ggp")
def ggp():
    return render_template("ggp.html")

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 404 status explicitly
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
