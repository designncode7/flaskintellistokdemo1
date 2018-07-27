"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template
from IntellistokDemoFlaskWeb2018Jul264 import app, errors
from azure.servicebus import ServiceBusService, Message, Queue


@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    bus_service = ServiceBusService(
    service_namespace='svcbusqueintellidemo',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='T5rIqHdGAM9/c1DtorXuyX6Rh3sxzHizri8UpNRqg+o='
    )

    try:
        iotmsg = bus_service.receive_queue_message('iothubqueuefri27-ns', peek_lock=False)
    except Exception as e:
          return render_template('500.html'), 500

    """Renders the home page."""
    return render_template(
        'index.html',
         title = "Intellistok Demo",
         datetimeheader = "Data: ",
         datetimecontent = iotmsg.body
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
