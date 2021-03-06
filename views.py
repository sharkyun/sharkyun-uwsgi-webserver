import time, json

# 导入模块中函数
import cache
from models import mysql_conn, mysql_query, mysql_close


def handler_index():
    """
    以二进制方式返回首页文件的内容，并替换文件中的变量为当前时间
    """
    dt = time.strftime(r"%Y%-m-%d %H:%M:%S")
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        content = content.replace("{{now_dt}}", dt)
    return bytes(content, encoding='utf-8')


def handler_css():
    with open('bootstrap/css/bootstrap.css', 'rb') as f:
        return f.read()


def server_data():
    conn, cursor = mysql_conn()
    sql = 'select id, host_name, os from base_info;'
    ret = mysql_query(cursor, sql)
    mysql_close(cursor, conn)
    return ret


def server_list():
    tab_tr_tpl = '''
            <tr>
                <td>{id}</td>
                <td>{host_name}</td>
                <td>{os}</td>
            </tr>
    '''
    
    ret = server_data()
    
    tab_tr = ''
    for item in ret:
        tab_tr += tab_tr_tpl.format(**item)
    
    with open('templates/server_list.html', 'r', encoding='utf-8') as f:
        content = f.read()
        content = content.replace('{{table_tr}}', tab_tr)
        content = content.replace('{{cache}}', '未使用缓存')
        content = content.replace('{{dt}}', "")
    return bytes(content, encoding='utf-8')


def cache_or_mysql():
    start_dt = time.time()
    rs = cache.rs
    ttl = rs.ttl("server_info")
    if ttl >= 1:
        cache_stat = '使用缓存'
        server_info = rs.get("server_info")
        server_info = json.loads(server_info)
    else:
        cache_stat = '未使用缓存'
        server_info = server_data()
        rs.set("server_info", json.dumps(server_info), ex=30)
    end_dt = time.time()
    use_dt = end_dt - start_dt

    tab_tr_tpl = '''
        <tr>
            <td>{id}</td>
            <td>{host_name}</td>
            <td>{os}</td>
        </tr>
        '''
    tab_tr = ''
    for item in server_info:
        tab_tr += tab_tr_tpl.format(**item)
    
    with open('templates/server_list.html', 'r', encoding='utf-8') as f:
        content = f.read()
        content = content.replace('{{table_tr}}', tab_tr)
        content = content.replace('{{cache}}', cache_stat)
        content = content.replace('{{dt}}', str(use_dt))
    return bytes(content, encoding='utf-8')

def serve_json():
    data = server_data()
    return json.dumps(data, indent=4).encode()

def weixin():
    with open('images/wx.jpeg', 'rb') as f:
        return f.read()

def zhihu():
    with open('images/zhihu.jpeg', 'rb') as f:
        return f.read()