import redis

from settings import CACHE_SERVER

# 缓存 Redis 连接信息
redis_host, redis_port = CACHE_SERVER.get("host"), CACHE_SERVER.get("port")
redis_db = CACHE_SERVER.get("db")

rs = redis.StrictRedis(
    host=redis_host,
    port=redis_port,
    db=redis_db
)
