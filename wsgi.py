import json

import views

headers = {
    # 文件扩展名               类型
    'html': ('Content-Type', 'text/html;charset=utf-8'),
    'json': ('Content-Type', 'application/json;charset=utf-8'),
    'css': ('Content-Type', 'text/css'),
    'jpg': ('Content-Type', 'application/x-jpg'),
    'jpeg': ('Content-Type', 'image/jpeg'),
    'png': ('Content-Type', 'image/png'),
}

urls = (
    ('/', views.handler_index, headers.get('html')),
    ('/bootstrap/css/bootstrap.css', views.handler_css, headers.get('css')),
    ('/server_list', views.server_list, headers.get('html')),
    ('/cache', views.cache_or_mysql, headers.get("html")),
    ('/api/server', views.serve_json, headers.get('json')),
    ('/images/wx.jpeg', views.weixin, headers.get('jpeg')),
    ('/images/zhihu.jpeg', views.zhihu, headers.get('jpeg')),
)

def application(env, start_response):
    for item in urls:
        url, handler_func, header = item
        print(env['PATH_INFO'], url)
        if env['PATH_INFO'] == url:
            start_response('200 OK', [header])
            return [handler_func()]
    
    start_response('404 OK', [('Content-Type', 'text/html')])
    return [b'404']