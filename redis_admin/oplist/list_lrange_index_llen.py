from redis_conn import redis_conn_util
if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(3)
    # lrange(name, start, end) 	返回key为name的list中start至end之间的元素
    users = coon.lrange("users",0,-1)
    for user in users:
        print(bytes(user).decode("utf-8"))
    # lindex(name, index) 返回key为name的list中index位置的元素
    user = coon.lindex("users", 1)
    print("users[1] = %s" % bytes(user).decode("utf-8"))
    # llen(name) 返回key为name的list的长度
    user_count = coon.llen("users")
    print("users中有%d个元素" % user_count)