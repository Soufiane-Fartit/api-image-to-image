from gevent.pywsgi import WSGIServer
from server_app import app
import os

port = int(os.environ.get('PORT', 33507))

http_server = WSGIServer(('', port), app)
http_server.serve_forever()