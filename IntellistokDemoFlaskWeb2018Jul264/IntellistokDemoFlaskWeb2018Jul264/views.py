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

    #bus_service = ServiceBusService(
    #service_namespace='svcbusqueintellidemo',
    #shared_access_key_name='RootManageSharedAccessKey',
    #shared_access_key_value='T5rIqHdGAM9/c1DtorXuyX6Rh3sxzHizri8UpNRqg+o=', 
    #)

    #queue_options = Queue()
    #queue_options.timeout = 1
    #iotmsg = bus_service.receive_queue_message('iothubqueuefri27-ns', peek_lock=False)
    

    """Renders the home page."""
    return render_template(
        'index.html',
         title = "IS&P DT&IoT",
         #datetimeheader = "Data: ",
         #datetimecontent = "Testing",
         year = datetime.now().year
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About This Web App',
        year=datetime.now().year,
        message='Intellistok Demo Web Application created with Flask Micro Framework.'
    )
