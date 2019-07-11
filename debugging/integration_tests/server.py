# ======================================================================================================================
#                                            DO NOT EDIT THIS FILE
# ======================================================================================================================

from wsgiref.simple_server import make_server
import urllib.parse
import threading
import time

import features

feature_dispatch = {
    '/encrypt': features.encrypt,
    '/decrypt': features.decrypt,
    '/random_key': features.random_key,
    '/random_encrypt': features.random_encrypt
}


def dispatch(environ, start_response):
    path = environ['PATH_INFO']
    qs = environ.get('QUERY_STRING', '')
    query = urllib.parse.parse_qs(qs)
    clean_query = {k: v[0] for k, v in query.items()}

    if path in feature_dispatch:

        # The returned object is going to be printed
        content = feature_dispatch[path](**clean_query)

        status = '200 OK'  # HTTP Status
        headers = [('Content-type', 'application/json; charset=utf-8')]  # HTTP Headers
        start_response(status, headers)

        return [str(content).encode('utf-8')]

    else:
        status = '400 Bad Request'  # HTTP Status
        headers = [('Content-type', 'plain/text; charset=utf-8')]  # HTTP Headers
        start_response(status, headers)

        return [b'This service does not exist']


httpd = make_server('', 8000, dispatch)


def start_server():
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=False)
    server_thread.start()
    time.sleep(1)
    print("Serving on port 8000.")


def stop_server():
    httpd.shutdown()