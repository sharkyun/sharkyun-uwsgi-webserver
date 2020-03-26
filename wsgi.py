import json

import views

headers = {
    'html': ('Content-Type', 'text/html;charset=utf-8'),
    'json': ('Content-Type', 'application/json;charset=utf-8'),
    'css': ('Content-Type', 'text/css'),
    'jpg': ('Content-Type', 'application/x-jpg'),
    'png': ('Content-Type', 'image/png'),
}

def application(env, start_response):
    if env['PATH_INFO'] == '/':
        start_response('200 OK', [('Content-Type','text/html')])
        return [views.handler_index()]
    elif env['PATH_INFO'] == '/bootstrap/css/bootstrap.css':
        start_response('200 OK', [('Content-Type', 'text/css')])
        return [views.handler_css()]
    elif env['PATH_INFO'] == '/server_list':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [views.server_list()]
    elif env['PATH_INFO'] == '/api/server':
        start_response('200 OK', [('Content-Type', 'application/json')])
        data = views.server_data()
        return [bytes(json.dumps(data), encoding='utf-8')]