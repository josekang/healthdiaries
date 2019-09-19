#########################################################
####### CREATE THE IMPORTS FOR THE CONTACT VIEWS ########
#########################################################

from flask import Blueprint, render_template, url_for, redirect, flash, request
from myproject.contact.forms import ContactForm
from myproject import mail
from flask_mail import Message

#########################################################
##### CREATE THE VIEWS FOR THE CONTACT FORM #############
#########################################################

contact_blueprint = Blueprint("contact", __name__, template_folder = "templates/contact")

@contact_blueprint.route("/contact", methods = ["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required")
            return render_template("contact.html", form = form)

        else:
            msg = Message(form.subject.data, sender = "josekangethe2@gmail.com", recipients = ["arigabrian.5@gmail.com"])
            msg.body = """
            From: %s &lt;%s&gt;
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template("contact.html", success = True)

    elif request.method == "GET":
        return render_template("contact.html", form = form)
