"""
The flask application package.
"""

from flask import Flask, Response
import time
from azure.servicebus import ServiceBusService, Message, Queue

app = Flask(__name__)

@app.route('/event_stream')
def stream():
    def event_stream():
        while True:
            bus_service = ServiceBusService(
                service_namespace='svcbusqueintellidemo',
                shared_access_key_name='RootManageSharedAccessKey',
                shared_access_key_value='T5rIqHdGAM9/c1DtorXuyX6Rh3sxzHizri8UpNRqg+o=', 
            )

            iotmsg = bus_service.receive_queue_message('iothubqueuefri27-ns', peek_lock=False)

            #time.sleep(3)
            yield 'data: %s\n\n' % iotmsg.body

    return Response(event_stream(), mimetype="text/event-stream")


import IntellistokDemoFlaskWeb2018Jul264.views
