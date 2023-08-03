from wsgiref.simple_server import make_server


def application(env, start_response):
    path = env.get('PATH_INFO')
    if path == '/':
        response_body = b'This is the root url'
    else:
        response_body = b'Hi! you go further then root.'

    status = '200 OK'
    response_headers = [('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]


httpd = make_server('127.0.0.1', 8051, application)

httpd.serve_forever()
