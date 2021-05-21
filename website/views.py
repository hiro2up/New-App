# Here goes everything that is not related to authentication
from flask import Blueprint, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

