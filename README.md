# sharkyun-uwsgi-webserver
 一个使用 python 语言编写的简单网站，用于学习演示

# 部署

## 安装依赖包

```python
$ cd sharkyun-uwsgi-webserver
$ sudo pip3 install  -r requirements.txt
```

## 配置说明

> 需要自己安装 MySQL  redis

`settings.py` 文件中配置数据库相关信息

```python
DB_SERVER = {
    "host": 'Mysql 数据 IP',
    "port": 3306,
    "user": 'MySQl 用户',
    "password": '密码',
    "db": 'database name 库名'
}

CACHE_SERVER = {
    "host": 'redis 服务的 IP',
    "port": 6379,
    'db': 0
}
```

`webserver.ini` 中有关于服务启动的参数

```ini
[uwsgi]
http = 127.0.0.1:8081
chdir = /此项目的根路径/sharkyun-uwsgi-webserver
wsgi-file = wsgi.py
processes = 4
threads = 2
virtualenv = /此项目的虚拟环境路径/.virtualenvs/uwsgi-webserver
```

> - http 监听地址和端口，就是浏览器访问的地址
> - wsgi-file 服务的启动文件
> - processes 开启 4 个进程
> - threads   每个进程开启 2 个线程

## 部署

### 1. 安装依赖包

> `$` 为命令提示符

```shell
$ cd sharkyun-uwsgi-webserver
$ pip3 install -r requiements.txt
```

### 2. 启动服务

```shell
$ uwsgi webserver.ini
```

### 3. 使用浏览器访问
> 主机检查服务器的防火墙设置
