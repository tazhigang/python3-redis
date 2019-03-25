from redis_conn import redis_conn_util
if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(3)
    # lset(name, index, value) 给key为name的list中index位置的元素赋值，越界则报错 True/False
    bool = coon.lset("users",0,"zhangba")
    print(bool)
    # lrem(name, count, value) 删除count个key的list中值为value的元素 返回删除的个数
    count = coon.lrem("users",2,"张三")
    print(count)