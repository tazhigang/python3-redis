from redis_conn import redis_conn_util
if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(5)
    # zadd(name, args, *kwargs)
    # 向key为name的zset中添加元素member，score用于排序。如果该元素存在，则更新其顺序
    count = coon.zadd("grade",{"Bob":100,"Mike":98})
    print(count)
    # zrem(name, *values)
    print(coon.zrem("grade","n1"))
    # 删除key为name的zset中的元素
