from redis_conn import redis_conn_util

if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(1)
    # mset与mget类似于redis命令中的mget,mset
    # msetnx msetex:批量添加及批量设置有效时间与if not exsist
    coon.mset({"a":"a","b":"b"})
    keys = coon.mget(["a","b"])
    for key in keys:
        print("%s------>%s" %((bytes(key).decode("utf-8")),bytes(coon.get(key)).decode("utf-8")))