from flask.templating import render_template
from . import pages

@pages.route('/')
def homepage():
    return render_template('home.html')