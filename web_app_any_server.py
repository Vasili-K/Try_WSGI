# To run this application as an example
# pip install waitress (if not installed)
# waitress-serve --listen=127.0.0.1:8051 web_app_any_server:application
# it will work on any WSGI complaint server

def application(environment, start_response):
    parameters = environment.get('QUERY_STRING')

    if not parameters:
        response_body = b'<h1 style="color:red">Sorry, I do not know yoi...</h1>'
    else:
        key, value = parameters.split('=')
        if key == 'id' and value == '35':
            response_body = b'<h1 style="color:green">I have been waiting for you!</h1>'
        else:
            response_body = b'<h1 style="color:blue">I know you, but you are not the one!</h1>'
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [response_body]
