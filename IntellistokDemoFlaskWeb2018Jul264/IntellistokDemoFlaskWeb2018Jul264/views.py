"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from IntellistokDemoFlaskWeb2018Jul264 import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    #html_content = "<html><head><title>Intellistok Demo</title></head><body>"
    #html_content += "<strong>Here are the measurements taken </strong> on " + formatted_now
    #html_content += "</body></html>"
    #return html_content

    """Renders the home page."""
    
    return render_template(
        'index.html',
         title = "Intellistok Demo",
         message = "Data measured",
         content = " on " + formatted_now
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
