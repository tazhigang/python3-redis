from redis_conn import redis_conn_util
if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(3)
    coon.lrange("user",0,-1)
    # # lpush(name, *values) 在key为name的list头添加值为value的元素，可以传多个
    # # rpush(name, *values) 在key为name的list尾添加值为value的元素，可以传多个
    # coon.lpush("user","张三","张四","张五","张六","张七","张八")
    # coon.lpush("users", "张二")
    # coon.rpush("users","张九")
    # rpop(name) 返回并删除key为name的list中的尾元素
    # lpop(name) 返回并删除key为name的list中的首元素
    user = coon.lpop("users")
    print(bytes(user).decode("utf-8"))
    # 以下适用于redis的消息队列
    # blpop(keys, timeout=0) 返回并删除名称为在keys中的list中的首元素，如果list为空，则会一直阻塞等待
    # brpop(keys, timeout=0) 返回并删除key为name的list中的尾元素，如果list为空，则会一直阻塞等待
