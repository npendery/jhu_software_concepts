from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__, template_folder='../templates', static_folder='../static')


@pages_bp.route('/')
def home():
    """
    Render the home page.
    """
    return render_template('home.html', active_page='home')

@pages_bp.route('/contact')
def contact():
    """
    Render the contact page.
    """
    return render_template('contact.html', active_page='contact')

@pages_bp.route('/projects')
def projects():
    """
    Render the projects page.
    """
    return render_template('projects.html', active_page='projects') 
