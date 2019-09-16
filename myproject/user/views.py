#########################################################
### CREATE THE NECESSARY IMPORTS FOR THE USER VIEWS #####
#########################################################

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import logout_user, login_user, login_required
from myproject import db
from myproject.user.models import User
from myproject.user.forms import  RegisterUserForm, LoginUserForm

#####################################################
#### NOW CREATE THE VIEWS FOR THE USER ##############
#####################################################

user_blueprint = Blueprint("user", __name__, template_folder = "templates/user")

@user_blueprint.route("/welcome")
@login_required
def welcome():
    return render_template("welcome.html")

@user_blueprint.route("/logout")
def logout():
    logout_user()
    flash("You have logged out Successfully!!!")
    return render_template("home.html")

@user_blueprint.route("/login", methods  = ["GET", "POST"])
def login():
    form = LoginUserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("You have logged in Successfully")
            next = request.args.get("next")
            if next == None or not next[0] == "/":
                next = url_for("user.welcome")
            return redirect(next)

    return render_template("login.html", form = form)

@user_blueprint.route("/register", methods = ["GET", "POST"])
def register():
    form = RegisterUserForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have Successfully created an account with our website")

        return redirect(url_for("user.login"))

    return render_template("register.html", form = form)
