import time

# 导入模块中函数
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
    return bytes(content, encoding='utf-8')