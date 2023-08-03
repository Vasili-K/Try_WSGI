from wsgiref.simple_server import make_server


# make_server creates a WSGI compliant server provided by Python


def application(env, start_response):
    """
    This function presents a Web Application.
    To interact with WSGI Web Server, Web Application needs to be WSGI compliant:
    1. it must accept two arguments
    2. second argument is callable
    :param env: a variable containing various information about the request
    :param start_response: is used to notify the server of the status of response and for setting various headers
    :return: WSGI server expects the return from application to be an iterable
    """
    path = env.get('PATH_INFO')
    if path == '/':
        response_body = b'This is the root url'
    else:
        response_body = b'Hi! you go further then root.'

    status = '200 OK'
    response_headers = [('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]


# httpd is the Web Server
# The first and second argument to make_server specifies the host and port
# on which the server will listen for requests
# Third argument to make_server passes the Web Application which the Web Server would use to get the response

httpd = make_server('127.0.0.1', 8051, application)

httpd.serve_forever()
