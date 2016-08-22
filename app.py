import os

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    html = '<body bgcolor=blue><H1>Hello KCPS!</H1></body>'
    hostname = os.uname()[1]
    return [html.encode(), hostname.encode()]

from wsgiref import simple_server

if __name__ == '__main__':
    server = simple_server.make_server('', 8080, application)
    server.serve_forever()
    
