from redis_conn import redis_conn_util

if __name__ == '__main__':
    coon = redis_conn_util.Redis_Conn.get_windows_coon(1)
    # 添加字符串 ex表示超时时间 nx表示 if not exsist
    coon.set("name", "张三", ex=60, nx=True)
    t1 = coon.ttl("name")  # 查看key对应value的剩余生效时间
    print("redis中通过键name所获取的value的剩余生效时间是%d s" % t1)
    # 添加字符串 不添加超时时间
    coon.set("age", 18)
    # 获取字符串
    age = coon.get("age")
    name = coon.get("name")
    # age name 是bytes类型的数据所以需要解码 以下是验证输出语句
    print("python中通过键age所获取的value在python中的数据类型%s" % type(age))
    print("redis中通过键age所获取的value的数据类型%s" % coon.type("age"))
    print("python中通过键name所获取的value在python中的数据类型%s" % type(name))
    print("redis中通过键name所获取的value的数据类型%s" % coon.type("age"))
    print("age=%s" % bytes(age).decode("utf-8"))  # 存储的时候是以utf-8的编码存储的，所以解码也需要utf-8
    print("name=%s" % bytes(name).decode("utf-8"))
