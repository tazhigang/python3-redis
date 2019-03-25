from redis_conn import redis_conn_util

if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(1)
    keys = coon.keys(pattern="*")  # 对应redis中的命令 keys *
    for key in keys:
        # 存储的时候是以utf-8的编码存储的，所以解码也需要utf-8
        print("%s------>%s" % (bytes(key).decode("utf-8"), bytes(coon.get(key)).decode("utf-8")))