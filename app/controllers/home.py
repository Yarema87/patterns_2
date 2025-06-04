from flask import Blueprint, render_template

mode_home = Blueprint('home', __name__)


@mode_home.route('/')
def index():
    return render_template('home.html')
