import pymysql

from settings import DB_SERVER

# 数据库连接信息
db_host, db_port = DB_SERVER.get("host"), DB_SERVER.get("port")
db_user, db_pass = DB_SERVER.get("user"), DB_SERVER.get("password")
db_db_name = DB_SERVER.get("db")
db_char = DB_SERVER.get('char') if DB_SERVER.get('char') else 'utf8mb4'

def mysql_conn():
    """
    创建连接
    返回连接对象，游标对象
    """
    conn = pymysql.connect( host=db_host,
                            port=db_port,
                            user=db_user,
                            passwd=db_pass, 
                            db=db_db_name,
                            charset=db_char)
    # 获取游标对象
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor


def mysql_query(cursor, query_sql):
    cursor.execute(query_sql)

    return cursor.fetchall()

def mysql_close(cursor, conn):
    # 关闭游标对象
    cursor.close()

    # 关闭连接对象
    conn.close()



##################### 示例数据 ##################

"""
dic =  {
    "base_info": {
        "host_name": "nginx_server",
        "kernel": "3.10.0-957.21.3.el7.x86_64",
        "os": "CentOS Linux release 7.6.1810 (Core)",
        'manufacturer': 'Alibaba Cloud',
        'pod_name': 'Alibaba Cloud ECS',
        'sn': '0f7e3d86-7742-4612-9f93-e3a9e4754199',
        'cpu_name': 'Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz',
        'cpu_num': 2,
        'cpu_cores_each': 4
    },
    "mem": [{
            'capacity': '8192 MB',
            'slot': 'DIMM_A3',
            'model': 'DDR3',
            'speed': '1333 MT/s',
            'manufacturer': '00CE04B380CE',
            'sn': '8362A2F8'
        },
        {
            'capacity': 'No Module Installed',
            'slot': 'DIMM_A4',
            'model': 'DDR3',
            'speed': 'Unknown',
            'manufacturer': '',
            'sn': ''
        }
    ]
}"""
