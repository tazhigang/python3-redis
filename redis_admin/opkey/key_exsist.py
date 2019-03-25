from redis_conn import redis_conn_util

if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(1)
    bool1 = coon.exists("a")
    # coon.exists("a") 判断键"a"是否存在 返回值是 数字类型 1:表示存在 0:不存在
    print("bool1的类型:%s,值是:%s" % (type(bool1),bool1))
    bool2 = coon.exists("aaaa")
    print("bool1的类型:%s,值是:%s" % (type(bool2), bool2))